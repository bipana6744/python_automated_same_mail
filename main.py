PLACEHOLDRER = '[name]'
with open("name_list.txt") as name:
    names = name.readlines()

# readlines helps to print in list

with open("./letters/starting_letter.txt") as letter:
    letter_contents = letter.read()
    for name in names:
        # strip helps to reduce gap
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDRER, stripped_name)
        with open(f"./letters/letter_for_{stripped_name}.txt", mode='w') as individual_letter:
            individual_letter.write(new_letter)