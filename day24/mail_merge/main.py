with open("./Input/Names/invited_names.txt") as names:
    name_list = names.readlines()
    names.close()

with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()
    letter.close()

for name in name_list:
    name = name.strip('\n')
    new_mail = template.replace("[name]", name)
    with open(f"./Output/ReadyToSend/letter_for_{name}", "w") as email_list:
        email_list.write(new_mail)
        email_list.close()
