items = ["Florida", "Georgia", "New York", "Texas", "Utah", "Arizona", "Idaho", "Wisconsin", "New Hampshire",
         "Washington", "Alabama", "Missippi", "Nevada", "New Jersay", "California", "Michigan", "Ohio", "Maine", "Vermont"]


length = len(items)


def hash_func(word):
    total = 1

    for letter in word:
        total *= (ord(letter) + 1)

    total = total ** 2
    total = total // len(word)

    return total


table = {hash_func(state): state for state in items}
print(table)


def find_item(hash):
    return table[int(hash)]


print(find_item(1562463960700692033245900800))
