letters = list(input("Please enter a string to test is a palindrome: "))

letters_stack = []

for e, letter in enumerate(letters):
    if len(letters_stack) == 0:
        letters_stack.append(letter)

    elif letters_stack[-1] != letter:
        letters_stack.append(letter)

    elif letters_stack[-1] == letter:
        del letters_stack[-1]

    if (e == (len(letters) // 2)) and (len(letters) % 2 != 0):
        del letters_stack[-1]


if len(letters_stack) == 0:
    print("That word was a palyndrome!")

else:
    print("That word was NOT a palyndrome :(")

