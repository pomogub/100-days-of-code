with open('Input/Names/invited_names.txt', 'r') as x:
    names = [name.strip() for name in x.readlines()]

with open('Input/Letters/starting_letter.txt', 'r') as y:
    template = y.read()
    for name in names:
        letter = template.replace('[name]', name)
        with open(f'Output/ReadyToSend/letter_to_{name}.docx', 'w') as z:
            z.write(letter)
