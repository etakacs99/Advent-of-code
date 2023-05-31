#Part one
file = open("inputs/day1.txt", "r")

sum_of_calories_per_elf = []
sum = 0

for calorie in file:
    if calorie == "\n": 
        sum_of_calories_per_elf.append(sum)   
        sum = 0
    else:
        sum = sum + int(calorie)

sum_of_calories_per_elf.sort()

print("DAY 1. - Part one")
print("THE ANSWER: The Elf with the most Calories is carrying a total of " + str(sum_of_calories_per_elf[-1]) + " Calories.")
file.close()

#Part two
print("DAY 1. - Part two")
sum_of_top_three = sum_of_calories_per_elf[-1] + sum_of_calories_per_elf[-2] + sum_of_calories_per_elf[-3]
print("THE ANSWER: The top three Elves with the most Calories are carrying a total of " + str(sum_of_top_three) + " Calories.")