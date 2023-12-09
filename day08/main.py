from art import logo

print(logo)


def caeser(text,shift,direction):
  result = ""
  if direction == "decode":
    shift *= -1
  for word in text:
    if word.isalpha():
      ind  = (alphabet.index(word) + shift) % 26
      result += alphabet[ind]
    else:
      result += word
  print(f"The {direction} text is {result}")

choice = True
  
while choice:
  alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(text,shift,direction)
  user_choice = input("Type 'yes' if you want to go again, Otherwise type 'no'")
  if user_choice == "no":
    choice = False
    print("Goodbye")
