import csv
import random
import datetime
import os.path


def start_quiz():
    """ starts the quiz, iterates over questions,
    checks answers, calls function to save record
    """
    print("Welcome to my quiz!")

    # find out the user's name
    user_name = input('What is your name? ')
    print('It is nice to meet you,', user_name)

    # get a list of questions once
    question_list = get_questions('my_questions_answers.csv')
    # determine max number of questions
    max_questions = len(question_list)

    # find out how many questions the quiz will have
    number_questions = None
    while number_questions is None:
        number_questions = ask_for_number_questions(max_questions)

    # initialize score to 0
    score = 0

    # ask as many questions as the user wanted
    for counter in range(number_questions):

        if counter == 0:
            print('My first question for you is:')

        if counter > 0:
            print('My next question for you is:')

        # get the next question from the question list
        question, answers, solution = get_next_question(question_list, counter)

        # displaying the question
        print(question)

        # displaying the answers
        for answer in answers:
            print(answer)

        # ask for user's answer
        ask_answer = input(
            "What do you think?\nPlease type a, b, or c to give an answer: ")

        # check user's answer
        # if it is correct
        if ask_answer == solution:
            print('Congrats! Your answer is correct.')
            score += 1

        # otherwise the answer was incorrect
        else:
            print()
            print('Your answer is is not correct.')
            print('The correct answer is:', solution)

        print()

    # put acsi trophy
    print_trophy()

    # final results are displayed to the user
    print('You went through all the questions.')
    print('You achieved', score, 'out of', number_questions, 'points.')
    print()

    # save results in csv file
    save_result(user_name, score, number_questions)


def ask_for_number_questions(max_questions):
    """ ask the user how many questions she wants to play until she gives a reasonable number

    Args:
        max_questions: is the maximum number of questions.

    Returns:
        the number of questions that the user requested (if valid) or None if invalid input
    """
    try:
        # try casting the input to an integer
        number_questions = int(
            input("How many questions do you want to answer today? "))

        # complain if number of requested questions is too big
        if number_questions > max_questions:
            print("Sorry, but I can only provide a maximum of", max_questions,
                  "questions today. Please enter a lower number.")
            return None

        # do not enter negative number of questions
        elif number_questions < 0:
            print("Are you serious?")
            return None

        # sensible input number
        return number_questions

    # if the input was not an integer throw error
    except ValueError:
        print('This is not a number.')

    return None


def get_questions(csv_file):
    """ read in questions from csv file and put them into a list

    Args:
        csv_file: the csv file from which the questions are retrieved.

    Returns:
       a list of questions
    """
    question_list = []
    with open(csv_file) as question_file:
        my_questions = csv.DictReader(question_file)
        for quest_dict in my_questions:
            question_list.append(quest_dict)

        # optional: shuffle
        random.shuffle(question_list)

    return question_list


def get_next_question(question_list, counter):
    """ take a question from the list at the index counter

    Args:
        question_list: the question list.
        counter: index of the current question in the question list.

    Returns:
       the current question as a tuple (question, (ans_a, ans_b, ans_c), correct_ans)
    """
    # get current question
    current_question = question_list[counter]

    # return tuple in form (question, (ans_a, ans_b, ans_c), correct_ans)
    return (current_question['question'],
            (current_question['answer a'],
             current_question['answer b'],
             current_question['answer c']),
            current_question['correct'])


def save_result(name, achieved_score, total_score):
    """ save the results from the quiz to results.csv

    Args:
        name: the user name.
        achieved_score: the score that the user achieved.
        total_score: the total score that the user could have achieved.
    """
    # check if the file exists
    file_exists = os.path.isfile('results.csv')

    with open('results.csv', "a") as result_file:
        # create the fieldnames
        fieldnames = ['name', 'achieved score', 'total score', 'time']
        # use the DictWriter to write the record to the file
        writer = csv.DictWriter(result_file, fieldnames=fieldnames)

        # if the file does not exist, write the header into the file
        if not file_exists:
            writer. writeheader()

        # write the record to the file
        writer.writerow({'name': name,
                         'achieved score': achieved_score,
                         'total score': total_score,
                         'time': datetime.datetime.now()})


def print_trophy():
    """ display a rewarding trophy
    """
    print("==========================================")
    print()
    print('             ___________ ')
    print("            '._==_==_=_.' ")
    print('            .-\:      /-. ')
    print('           | (|:.     |) | ')
    print("            '-|:.     |-' ")
    print('              \::.    / ')
    print("               ': : .' ")
    print('                 ) ( ')
    print("               _.' '._ ")
    print('          jgs `"""""""` ')
    print()


# calling the function that starts the quiz
start_quiz()
