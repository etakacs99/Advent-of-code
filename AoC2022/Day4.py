file = open("inputs/day4.txt", "r")

sum_of_fully_contain = 0
sum_of_overlap = 0
for pair in file: 
    temp_pair = pair.strip().split(",")
    first_half = temp_pair[0].split("-")
    list_first_half = [*range(int(first_half[0]), int(first_half[1]) + 1, 1)]
    second_half = temp_pair[1].split("-")
    list_second_half = [*range(int(second_half[0]), int(second_half[1]) + 1, 1)]
    #Part one
    if all(elem in list_first_half for elem in list_second_half) or all(elem in list_second_half for elem in list_first_half): 
        sum_of_fully_contain = sum_of_fully_contain + 1
    #Part two
    if any(elem in list_first_half for elem in list_second_half) or any(elem in list_second_half for elem in list_first_half):
        sum_of_overlap = sum_of_overlap + 1
file.close()

print("DAY 4. - Part one")
print("THE ANSWER: In " + str(sum_of_fully_contain) + " assignment pairs do (one range) fully contain the other.")

print("DAY 4. - Part two")
print("THE ANSWER: In " + str(sum_of_overlap) + " assignment pairs do the ranges overlap.")