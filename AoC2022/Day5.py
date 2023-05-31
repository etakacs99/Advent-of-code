def getResultMessage(list):
    message = ""
    for stack in list:
        message += str(stack.pop())
    return message

#my_input
#[N] [G]                     [Q]    
#[H] [B]         [B] [R]     [H]    
#[S] [N]     [Q] [M] [T]     [Z]    
#[J] [T]     [R] [V] [H]     [R] [S]
#[F] [Q]     [W] [T] [V] [J] [V] [M]
#[W] [P] [V] [S] [F] [B] [Q] [J] [H]
#[T] [R] [Q] [B] [D] [D] [B] [N] [N]
#[D] [H] [L] [N] [N] [M] [D] [D] [B]
# 1   2   3   4   5   6   7   8   9
file = open("inputs/day5.txt", "r")
my_stack_list_one = [
    ['D','T','W','F','J','S','H','N'],
    ['H','R','P','Q','T','N','B','G'],
    ['L','Q','V'],
    ['N','B','S','W','R','Q'],
    ['N','D','F','T','V','M','B'],
    ['M','D','B','V','H','T','R'],
    ['D','B','Q','J'],
    ['D','N','J','V','R','Z','H','Q'],
    ['B','N','H','M','S']
    ]

my_stack_list_two = [
    ['D','T','W','F','J','S','H','N'],
    ['H','R','P','Q','T','N','B','G'],
    ['L','Q','V'],
    ['N','B','S','W','R','Q'],
    ['N','D','F','T','V','M','B'],
    ['M','D','B','V','H','T','R'],
    ['D','B','Q','J'],
    ['D','N','J','V','R','Z','H','Q'],
    ['B','N','H','M','S']
    ]

for line in file:
    movement = line.strip().split(" ")
    amount = int(movement[1])
    where_from = int(movement[3]) - 1
    where_to = int(movement[5]) - 1
    #Part one
    for i in range(amount):
        crate_part_one = my_stack_list_one[where_from].pop()
        my_stack_list_one[where_to].append(crate_part_one)
    #Part two
    crate_part_two = my_stack_list_two[where_from][-amount:]
    my_stack_list_two[where_from] = my_stack_list_two[where_from][:-amount]
    my_stack_list_two[where_to].extend(crate_part_two)

file.close()

print("DAY 5. - Part one")
print("THE ANSWER: (CrateMover 9000) After the rearrangement procedure completes, " + getResultMessage(my_stack_list_one) + " crate ends up on top of each stack")

print("DAY 5. - Part two")
print("THE ANSWER: (CrateMover 9001) After the rearrangement procedure completes, " + getResultMessage(my_stack_list_two) + " crate ends up on top of each stack")