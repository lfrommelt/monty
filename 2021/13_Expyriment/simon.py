from expyriment import design, control, stimuli, misc

POSITIONS = {
    "left": (-300, 0),
    "right": (300, 0),
}

COLORS = {
    "red": (255, 0, 0), 
    "green": (0, 128, 0)
}

KEY_MAPPING = {
    misc.constants.K_s: "left", 
    misc.constants.K_l: "right"
}

PAIRINGS = {
    "red_left_green_right": ("s", "l"),
    "red_right_green_left": ("l", "s")
}

INSTRUCTION_TEXT = """ 
Here's  your task: You will see a colored dot. \n 
If  the dot is red, press the key '{}'. \n 
If  the dot is green, press the key '{}'.
"""




def perform_simon_task():
    """Performs a Simon Task experiment."""

    exp = design.Experiment("Simon Task")
    control.initialize(exp)
    
    exp = design_experiment(exp, POSITIONS, COLORS, PAIRINGS)

    exp.data_variable_names = ["pairing", "position", "color", "key", "reaction_time"]

    control.start()
    execute_experiment(exp, INSTRUCTION_TEXT, KEY_MAPPING, PAIRINGS)
    control.end()


def execute_experiment(exp, text, key_mapping, pairings):
    """Executes a predesigned Simon Task."""

    fixcross = stimuli.FixCross()
    fixcross.preload()

    for block in exp.blocks:

        pairing = pairings[block.get_factor("pairing")]
        instructions = text.format(*pairing)

        stimuli.TextScreen("Instructions", instructions).present()
        exp.keyboard.wait()

        for trial in block.trials:

            fixcross.present()

            exp.clock.wait(1000 - trial.stimuli[0].preload())
            trial.stimuli[0].present()

            key, rt = exp.keyboard.wait(keys=key_mapping.keys())

            exp.data.add([block.get_factor("pairing"), trial.get_factor("position"), trial.get_factor("color"), key_mapping[key], rt])
    


def design_experiment(exp, positions, colors, pairings):
    """Designs a Simon Task experiment."""

    for pair_name, pairing in pairings.items():
        
        b = design.Block()
        b.set_factor("pairing", pair_name) 

        for pos_name, position in positions.items():
            for color_name, color in colors.items():

                t = design.Trial()
                t.set_factor("position", pos_name)
                t.set_factor("color", color_name)
                s = stimuli.Rectangle((50, 50), position=position, colour=color)
                t.add_stimulus(s)
                b.add_trial(t, copies=2)

        b.shuffle_trials()
        exp.add_block(b)
        
    return exp
            


if __name__ == "__main__":
    perform_simon_task()
