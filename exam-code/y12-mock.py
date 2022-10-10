remaining_letters = ["a", "z", "s", "q"]
answer = "test"

for i in answer:
    if i in remaining_letters:
        for e, j in enumerate(remaining_letters):
            if j == i:
                del remaining_letters[e]
                break
            if i == remaining_letters[-1]:
                print(1)
        
    else: 
        print(0)