from functools import cmp_to_key
# Returns 1 if x is less than y.
# Returns 0 if x equals y.
# Returns -1 if x is greater than y.
def compare(x, y) -> int:
    if isinstance(x, list) and isinstance(y, int):
        y = [y]
    
    if isinstance(x, int) and isinstance(y, list):
        x = [x]
    
    if isinstance(x, int) and isinstance(y, int):
        if x < y: 
            return 1
        if x == y:
            return 0
        return -1

    if isinstance(x, list) and isinstance(y, list):
        i = 0
        while i < len(x) and i < len(y):
            c = compare(x[i], y[i])
            if abs(c) == 1 :
                return c 
            i += 1

        if i == len(x):
            return 0 if len(x) == len(y) else 1  # If the return value is 1 x list ended first.
            
        # If i didn't hit the end of a, it hit the end of b first
        # This means that b is shorter, which is bad (if i == len(y))
        return -1
            
def main():
    with open("inputs/day13.txt") as f:
        pairs1 = f.read().strip().split("\n\n")

    #Part one
    sum_of_indices = 0
    for i, element in enumerate(pairs1):
        #Eval: Turns any expression into a python Object. (The input lines are valid py expressions.)
        x, y = map(eval, element.split("\n"))
        if compare(x, y) == 1:
            sum_of_indices += (i + 1)

    print("DAY 13. - Part one")
    print(f"THE ANSWER: The sum of the indices of those pairs is {sum_of_indices}.")


    with open("inputs/day13.txt") as f:
        pairs2 = f.read().strip().replace("\n\n", "\n").split("\n")

    #Part two
    lists = list(map(eval, pairs2))

    #Adding divider packets
    lists.append([[2]])
    lists.append([[6]])

    #A key (function)can be given to the sorted function so he compares the lists with that method
    lists = sorted(lists, key=cmp_to_key(compare), reverse=True)

    for i, packet in enumerate(lists):
        #print(f"INDEX: {i + 1}, PACKET: {packet}")
        if packet == [[2]]:
            x = i + 1
        if packet == [[6]]:
            y = i + 1

    print("DAY 13. - Part two")
    print(f"THE ANSWER: The decoder key for the distress signal is {x*y}.")

if __name__=="__main__":
    main()