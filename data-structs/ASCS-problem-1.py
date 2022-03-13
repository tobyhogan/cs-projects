string = input("Please enter a string to test is a palindrome: ")

letters_stack = [None]

for i in string:
    if letters_stack[-1] != i:
        letters_stack.append(i)

    elif (letters_stack[-1]):
        letters_stack.pop()

    elif (len(string) % 2 != 0) and (i == string[len(string) // 2]):
        print("yo")
        letters_stack.pop()



if len(letters_stack) == 1:
    print("That text was a palindrome!")