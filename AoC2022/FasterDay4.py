def contains(first_range, second_range):
    return int(first_range[0]) <= int(second_range[0]) and int(second_range[1]) <= int(first_range[1])

def overlaps(first_range, second_range):
    return (int(first_range[0]) <= int(second_range[0]) and int(second_range[0]) <= int(first_range[1])) or(int(first_range[0]) <= int(second_range[1]) and int(second_range[1]) <= int(first_range[1])) 

file = open("inputs/day4.txt", "r")

sum_of_fully_contain = 0
sum_of_overlap = 0
for pair in file: 
    temp_pair = pair.strip().split(",")
    first_half = temp_pair[0].split("-")
    second_half = temp_pair[1].split("-")
    #Part one
    if contains(first_half, second_half) or contains(second_half, first_half): 
        sum_of_fully_contain = sum_of_fully_contain + 1
    #Part two
    if overlaps(first_half, second_half) or overlaps(second_half, first_half):
        sum_of_overlap = sum_of_overlap + 1
file.close()

print("DAY 4. - Part one")
print("THE ANSWER: In " + str(sum_of_fully_contain) + " assignment pairs do (one range) fully contain the other.")

print("DAY 4. - Part two")
print("THE ANSWER: In " + str(sum_of_overlap) + " assignment pairs do the ranges overlap.")