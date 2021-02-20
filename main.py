PLACEHOLDER = "[name]"

# create names list
all_lines = ''
with open('Input/Names/invited_names.txt') as file:
    all_lines = file.read()

name_list = all_lines.splitlines()


# for each name
for name in name_list[0:]:
    # create a new_letter with name in title in ReadyToSend
    with open(f'Output/ReadyToSend/letter_for_{name}.txt', mode='w') as new_letter:
        with open('Input/Letters/starting_letter.txt') as original_letter:
            # save original_letter's content in text as a string:
            text = original_letter.read()
            # replace [name] with element from name list
            text = text.replace(PLACEHOLDER, f"{name}")
            # insert text within created new_letter
            new_letter.write(text)
