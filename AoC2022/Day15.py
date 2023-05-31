#Source: https://www.youtube.com/watch?v=w7m48_uCvWI

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def main():
    # Read input
    with open("inputs/day15.txt") as f: 
        lines = f.read().strip().split("\n")
    
    # Parse input
    sensors = []
    beacons = []
    for line in lines:
        parts = line.split(" ")

        sensor_x = int(parts[2][2:-1])
        sensor_y = int(parts[3][2:-1])
        beacon_x = int(parts[8][2:-1])
        beacon_y = int(parts[9][2:])

        sensors.append((sensor_x, sensor_y))
        beacons.append((beacon_x, beacon_y))

    # Go through every sensor and find it's closest beacon.
    distances = []
    for i in range(len(sensors)):
        distances.append(distance(sensors[i], beacons[i]))

    # Go through every sensor and find intersection on the line y = 2000000
    y = 2000000
    intervals = []
    for i, s in enumerate(sensors):
        dx = distances[i] - abs(s[1] - y)
        if dx <= 0:
            continue
        intervals.append((s[0] - dx, s[0] + dx))

    # Find the overlaps on the intervall
    allowed_x = []
    for beacon_x, beacon_y in beacons:
        if beacon_y == y: 
            allowed_x.append(beacon_x)

    min_x = min([i[0] for i in intervals])
    max_x = max([i[1] for i in intervals])

    num_of_positions = 0
    for x in range(min_x, max_x + 1):
        if x in allowed_x:
            continue

        for left, right in intervals:
            if left <= x <= right:
                num_of_positions += 1
                break

    print("DAY 15. - Part one")
    print(f"THE ANSWER: In the row where y=2000000, {num_of_positions} positions cannot contain a beacon.")

    pos_lines = []
    neg_lines = []

    for i, s in enumerate(sensors):
        d = distances[i]
        neg_lines.extend([s[0] + s[1] - d, s[0] + s[1] + d])
        pos_lines.extend([s[0] - s[1] - d, s[0] - s[1] + d])

    positive = None
    negative = None

    for i in range(2 * len(sensors)):
        for j in range(i + 1, 2 * len(sensors)):
            a, b = pos_lines[i], pos_lines[j]

            if abs(a - b) == 2:
                positive = min(a, b) + 1

            a, b = neg_lines[i], neg_lines[j]

            if abs(a - b) == 2:
                negative = min(a, b) + 1

    x, y = (positive + negative) // 2, (negative - positive) // 2
    tuning_frequency = x * 4000000 + y

    print("DAY 15. - Part two")
    print(f"THE ANSWER: The tuning frequency of the only possible position for the distress beacon is: {tuning_frequency}")

if __name__=="__main__":
    main()