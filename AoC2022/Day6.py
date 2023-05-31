def areNotEqual(list):
    common_chars = set()
    for char in list: 
        common_chars.add(char)
    return len(common_chars)

file = open("inputs/day6.txt", "r")
line = file.readline().strip()
file.close()

first_part_done = False
i = 0
saved_chars = []
for char in line: 
    #Part one
    if not first_part_done and i >= 4:
        if areNotEqual(saved_chars[-4:]) == 4:
            result = i
            first_part_done = True
    #Part two
    if i >= 14:
        if areNotEqual(saved_chars[-14:]) == 14:
            break  
    saved_chars.append(char)
    i = i + 1


print("DAY 6. - Part one")
print("THE ANSWER: " + str(result) + " characters need to be processed before the first start-of-packet marker is detected")

print("DAY 6. - Part two")
print("THE ANSWER: " + str(i) + " characters need to be processed before the first start-of-packet marker is detected")