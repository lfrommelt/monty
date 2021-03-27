

# Source: https://www.nytimes.com/2018/12/12/technology/amazon-new-york-hq2-data.html

article = """High-Tech Degrees and the Price of an Avocado: The Data New York Gave to Amazon\n\nThe city and state sent loads of data to Amazon during its search for a new headquarters, offering a peek into the valuable information the company collected during the process.\n\nKaren Weise\n\nBy Karen Weise\n\n\tDec. 12, 2018\n\n[Updated Feb. 14: Amazon said it was canceling plans to build a corporate campus in New York City, after the deal had run into fierce opposition from local lawmakers who criticized providing subsidies to one of the world’s most valuable companies.]\n\nAn avocado at Whole Foods costs 1.25. \nColumbia University handed out 724 graduate degrees in computer science over the past three years. \nAnd 10 potential land parcels in Long Island City are zoned M1-4, for light manufacturing.\n\nNew York provided all of these data points, and thousands more, to Amazon as part of its successful bid to woo the tech giant to town.\n\nOn Monday, New York City posted online the 253-page proposal it submitted, along with New York State, to Amazon in March. \nThe city quickly took the file down, saying it should have checked with its partners before posting it, because the document included proprietary information. \nBut The New York Times downloaded the document before it was taken off the public website.\n\nThe proposal shows the types of data, some rarely available publicly, that the company amassed from cities across the country as part of its search for a second headquarters.
"""

##########################
# Task 2.1
# 

print("\nNow computing results for task 2.1 ...\n")

def make_nice(article):
    """Returns the given article nicely formatted."""

    lines = article.splitlines()

    lines = [line for line in lines if line != ""]

    nice = "\n" + "#" * 29 + " START OF TEXT " + "#" * 29 + "\n"
    nice += "\n" + lines[0] + "\n" + "\n"
    nice += lines[1] + "\n"  + "\n"
    nice += lines[3] + " - " + lines[4].strip() + "\n" + "\n"

    for index, line in enumerate(lines[6:]):
          nice += "{}: {}".format(index + 1, line) + "\n"

    nice += "\n" + "#" * 30 + " END OF TEXT " + "#" * 30 + "\n"
  
    return nice

article_nice = make_nice(article)
print(article_nice)

#########################
# Task 2.2
#

print("\nNow computing results for task 2.2 ...\n")

def frequency_dict(my_list):
    """Creates a dictionary from the frequencies of elements in a list."""

    frequencies = {}

    for element in set(my_list):
        n = my_list.count(element)
        if n > 1:
            frequencies[element] = n

    return frequencies


def max_key(my_dict):
    """Returns the key of the maximum value in a dictionary."""

    # there are many ways in Python to do this
    # this one only uses functions that we learned
    # in the lecture
    
    max_key = None

    for key, value in my_dict.items():
        if max_key == None or my_dict[key] > my_dict[max_key]:
            max_key = key

    return max_key

words = article_nice.split()
word_frequencies = frequency_dict(words)
max_word = max_key(word_frequencies)

print("The most frequent word is '{}' with {} occurrences.".format(max_word, word_frequencies[max_word]))

characters = list(article_nice)
char_frequencies = frequency_dict(characters)
max_char = max_key(char_frequencies)

print("The most frequent character is '{}' with {} occurrences.".format(max_char, char_frequencies[max_char]))

non_alphanumeric_chars = [c for c in characters if not c.isalnum()]
print("There are {} non-alphanumeric characters in the text.".format(len(non_alphanumeric_chars) - 118 - 8))


#########################
# Task 3.1
#

print("\nNow computing results for task 3.1 ...\n")


def caesar_cipher(text, shift=1):
    """Applies the Caesar Cipher to a given string."""

    text_decrypt = ""

    for character in text:

        uni_char = ord(character)

        if uni_char > 96 and uni_char < 123:
            uni_char_decrypt = 97 + (uni_char + shift - 97) % 26
            text_decrypt += chr(uni_char_decrypt)
        else:
            text_decrypt += character

    return text_decrypt


print(caesar_cipher(article_nice, 3))


#########################
# Task 3.2
#

print("\nNow computing results for task 3.2 ...\n")


def compute_shift(word_encrypted, word_original):
    """Computes the shift by comparing the first characters of two equivalent words."""

    uni_encrypted = ord(word_encrypted[0])
    uni_original = ord(word_original[0])
    
    print("The encryption was probably done with a shift of {}.".format(uni_encrypted - uni_original))
    
    return uni_original - uni_encrypted


secret_message = "vhgzktmnetmbhgl!%mabl%bl%max%lxvkxm%fxlltzx.%max%xgvhwbgz%ptl%whgx%pbma%max%yheehpbgz%labym:%fbgnl%lxoxg.%atox%t%gbvx%wtr."

# we compile a list of all non-alphabumeric characters in the secret message
non_alnum_chars = [character for character in secret_message if not character.isalnum()]

# we compute the most frequent non-alphanumeric character and assume it to be space " "
non_alnum_char_frequencies = frequency_dict(non_alnum_chars )
space_encrypt = max_key(non_alnum_char_frequencies)


# we replace all occurrences of the most frequent alphanumeric character with a space " "
secret_with_spaces = secret_message.replace(space_encrypt, " ")

# we split the secret message along  spaces
secret_words = secret_with_spaces.split()

# we compute the most frequent word and assume it to be "the", 
# since it is the most frequent word in English overall
secret_words_frequencies = frequency_dict(secret_words)
the_encrypt = max_key(secret_words_frequencies)

# we compute the shift needed to decrypt the secret message
decrypt_shift = compute_shift(the_encrypt, "the")

# we decrypt the secret message and print it
secret_decrypt = caesar_cipher(secret_with_spaces, decrypt_shift)
print(secret_decrypt)


