# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("./Input/Names/invited_names.txt") as names:
    guests = names.readlines()
    stripped_guest = []
    for guest in guests:
        stripped_guest.append(guest.strip())

with open("./Input/Letters/starting_letter.txt") as letter:
    invite_letter = letter.read()
    for guest in stripped_guest:
        new_letter = invite_letter.replace("[name]", guest)

        with open(
                f"./Output/ReadyToSend/letter_for_{guest}.txt", mode="w"
        ) as final_letter:
            final_letter.write(new_letter)
