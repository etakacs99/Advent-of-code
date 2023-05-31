filled_1 = set()
filled_2 = set()

def simulate_sand_part_one(max_y: int) -> bool:
    global filled_1
    # sand starts from
    x, y = 500, 0

    while y <= max_y:
        # sand falls straigth down
        if (x, y + 1) not in filled_1:
            y += 1
            continue
        
        # can't fall straigth down, move left down
        if (x - 1, y + 1) not in filled_1:
            x -= 1
            y += 1
            continue

        #can't fall left down, move right down
        if (x + 1, y + 1) not in filled_1:
            x += 1
            y += 1
            continue
    
        #Everything is filled, sand stops moving
        filled_1.add((x, y))
        return True

    #The sand never stops moving
    return False

def simulate_sand_part_two(max_y: int):
    global filled_2
    x, y = 500, 0

    if (x, y) in filled_2: 
        return (x, y)
    
    while y <= max_y:
        if (x, y + 1) not in filled_2:
            y += 1
            continue
        if (x - 1, y + 1) not in filled_2:
            x -= 1
            y += 1
            continue
        if (x + 1, y + 1) not in filled_2:
            x += 1
            y += 1
            continue

        #Everything filled
        break

    return (x, y)

def main():
    global filled_1
    global filled_2

    with open("inputs/day14.txt") as f:
        lines = f.read().strip().split("\n")

    for line in lines:
        coords = []

        # Process/parse input coordinates of the paths of rock
        for str_coord in line.split(" -> "):
            x, y = map(int, str_coord.split(","))
            coords.append((x, y))

        for i in range(1, len(coords)):
            current_x, current_y = coords[i]
            prev_x, prev_y = coords[i - 1]

            # fill in the gaps:
            # After the first point of each path, each point indicates the end of a 
            # straight horizontal or vertical line to be drawn from the previous point.

            #vertical
            if current_y != prev_y:
                assert current_x == prev_x
                for y in range(min(current_y, prev_y), max(current_y, prev_y) + 1):
                    filled_1.add((current_x, y))
                    filled_2.add((current_x, y))
            # horizontal
            if current_x != prev_x:
                assert current_y == prev_y
                for x in range(min(current_x, prev_x), max(current_x, prev_x) + 1):
                    filled_1.add((x, current_y))
                    filled_2.add((x, current_y))
        
    #the bottom line of the rock 
    max_y = max([coord[1] for coord in filled_1])

    sum_of_sand_units = 0
    while True:
        simulate = simulate_sand_part_one(max_y)
        if not simulate:
            break
        sum_of_sand_units += 1

    print("DAY 14. - Part one")
    print(f"THE ANSWER: {sum_of_sand_units} units of sand come to rest before sand starts flowing into the abyss below.")

    sum_of_sand_units = 0
    max_y = max([coord[1] for coord in filled_2])

    while True: 
        x, y = simulate_sand_part_two(max_y)
        filled_2.add((x, y))
        sum_of_sand_units += 1

        #stop condition, reached the sand pouring point
        if (x, y) == (500, 0):
            break

    print("DAY 14. - Part two")
    print(f"THE ANSWER: {sum_of_sand_units} units of sand come to rest.")

if __name__ == "__main__":
    main()