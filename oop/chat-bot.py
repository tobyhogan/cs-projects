from time import sleep

line_break = "=" * 53

questions = {"What is object oriented programming?":
             "A method of writing programs using encapsulated groups of attributes and methods."}
ans_correct = 0


def time():
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    sleep(1)


for key, value in questions.items():
    print(line_break)
    print("The quiz will now start.")
    print(line_break)
    print(f"Question {1}: {key}")
    print("")
    time()
    print("")
    print(f"Answer: {value}")
    print("Did you get that right?")
    print("Type yes or no")
    print(line_break)

    answer = input(">>> ")
    if answer.upper() == "YES":
        ans_correct += 1
