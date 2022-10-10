data = "0001001010101011011010010011010001010100011100100"

# the format for streak is [streak_length, binary state(1 or 0)]
compressed_data = []
last_character = None
current_streak = 0


for e, i in enumerate(data):
    if e != 0:
        if data[e] == data[e - 1]:
            current_streak += 1
            last_character = int(data[e])

        else:
            compressed_data += [current_streak, last_character]
            last_character = None
            current_streak = 0


print(compressed_data)
