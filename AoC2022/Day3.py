#Part one
file1 = open("inputs/day3.txt", "r")
#using ASCII code to calculate 
def find_priority(letter):
    if letter >= ord('a') and letter <= ord('z'):
        return letter - ord('a') + 1
    if letter >= ord('A') and letter <= ord('Z'): 
        return letter - ord('A') + 27

sum1 = 0
for items in file1:
    list_items = list(items.strip())
    first_compartment = list_items[:len(list_items)//2]
    second_compartment = list_items[len(list_items)//2:]
    common_characters = set(first_compartment).intersection(second_compartment)
    for char in common_characters: 
        sum1 = sum1 + find_priority(ord(char))
file1.close()

print("DAY 3. - Part one")
print("THE ANSWER: The sum of the priorities of those item types is: " + str(sum1))

#Part two
file2 = open("inputs/day3.txt", "r")
sum2 = 0
group = [] 
for items in file2:
    group.append(items.strip())
    if len(group) == 3:
        badge = set(list(group[0])).intersection(list(group[1])).intersection(list(group[2]))
        for char in badge:
            sum2 = sum2 + find_priority(ord(char))
        group.clear()
file2.close()

print("DAY 3. - Part two")
print("THE ANSWER: (three-Elf group) The sum of the priorities of those item types is: " + str(sum2))