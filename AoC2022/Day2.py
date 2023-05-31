#Part one
file = open("inputs/day2.txt", "r")
#A -> ROCK (X)
#B -> PAPER (Y)
#C -> SCISSOR (Z)
points = {
    'X':1,
    'Y':2,
    'Z':3
}

sum1 = 0
for battle in file:
    actions = battle.strip().split(" ")
    if (actions[0] == 'A' and actions[1] =='X') or (actions[0] == 'B' and actions[1] =='Y') or (actions[0] == 'C' and actions[1] =='Z'):
        #IT'S A DRAW!
        sum1 = sum1 + points[actions[1]] + 3
    elif (actions[0] == 'C' and actions[1] =='X') or (actions[0] == 'B' and actions[1] =='Z') or (actions[0] == 'A' and actions[1] =='Y'):
        #I WON!
        sum1 = sum1 + points[actions[1]] + 6
    else:
        #YOU LOST!
        sum1 = sum1 + points[actions[1]]
file.close()

print("DAY 2. - Part one")
print("THE ANSWER: My total score would be if everything goes exactly according to my strategy guide: " + str(sum1))

#Part two
file2 = open("inputs/day2.txt", "r")
sum2 = 0
for battle in file2:
    actions = battle.strip().split(" ")
    if (actions[1] == 'X'):
        # need to lose
        if actions[0] == 'A':
            sum2 = sum2 + points['Z']
        elif actions[0] == 'B':
            sum2 = sum2 + points['X']
        elif actions[0] == 'C':
            sum2 = sum2 + points['Y']
    elif (actions[1] == 'Y'):
        # must be draw
        if actions[0] == 'A':
            sum2 = sum2 + points['X'] +3
        elif actions[0] == 'B':
            sum2 = sum2 + points['Y'] +3
        elif actions[0] == 'C':
            sum2 = sum2 + points['Z'] +3
    elif(actions[1] == 'Z'):
        # need to win
        if actions[0] == 'A':
            sum2 = sum2 + points['Y'] + 6
        elif actions[0] == 'B':
            sum2 = sum2 + points['Z'] + 6
        elif actions[0] == 'C':
            sum2 = sum2 + points['X'] + 6
file2.close()

print("DAY 2. - Part two")
print("THE ANSWER: (Modifications) My total score would be if everything goes exactly according to my strategy guide: " + str(sum2))
