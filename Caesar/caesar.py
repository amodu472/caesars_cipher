"""This program defines a function that takes in a text and
encrypts/decrypts it into a ciphertext based on a provided key/shift value"""

alpha = [chr(i) for i in range(97, 123)]


# caesar function
def caesar(text_: str, s: int, action: str):
    """this function takes in text, shift and action as input, and "shifts" aka encodes/decodes the text"""
    cipher = ""
    action_list = ["encode"]

    if action.lower() == "decode":
        s *= -1
    elif action.lower() not in action_list:
        return "Invalid Encoding or Decoding option! Try again."

    for char in text_:
        if char in alpha:
            current_index = alpha.index(char)
            new_index = (current_index + s) % 26
            cipher += alpha[new_index]
        else:
            cipher += char
    return cipher


go_again = True
while go_again:
    text = input("Please enter plaintext: \n").lower()
    shift = int(input("Type the shift number: \n"))
    request = input("Encode or Decode text? \n").lower()

    print(caesar(text, shift, request))

    again = input("Would you like to go again? \n").lower()
    if again == "yes" or again == "y":
        continue
    else:
        print("Adios!")
        break
