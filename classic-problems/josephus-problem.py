circle = list(range(1, 101))
print(circle)
interval = 2
counter = 0

while len(circle) > 1:
    for person in circle:
        counter += 1
        if counter % interval == 0:
            circle.remove(person)
    print(circle)

print(circle)
