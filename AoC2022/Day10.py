def checkCycles():
    global cycle
    global sum_of_signal_strengths
    global x

    checkScreen()
    cycle = cycle + 1
    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
            sum_of_signal_strengths = sum_of_signal_strengths + (x * cycle)

#Part two
def checkScreen():
    global LETTER
    global crt_monitor
    global x
    global cycle

    row = cycle // 40
    col = cycle % 40 
    if x - 1 == col or x == col or x + 1 == col:
        crt_monitor[row][col] = LETTER

file = open("inputs/day10.txt", "r")
#Part one
x = 1
cycle = 0
sum_of_signal_strengths = 0

#Part two
LETTER = '█'
EMPTY  = ' '
crt_monitor = [[EMPTY for _ in range(40)] for _ in range(6)]

for line in file: 
    splited_line = line.strip().split(" ")
    checkCycles()
    if splited_line[0] == "addx":
        checkCycles()
        x = x + int(splited_line[1])
file.close()

print("DAY 10. - Part one")
print(f"THE ANSWER: The sum of these six signal strengths is: {sum_of_signal_strengths}")

print("DAY 10. - Part two")
print(f"THE ANSWER: The eight capital letters on my CRT:")
for i in range(len(crt_monitor)): 
    for j in range(len(crt_monitor[i])):
        print(crt_monitor[i][j], end="")
    print("")