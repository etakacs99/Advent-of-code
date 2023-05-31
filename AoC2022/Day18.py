import numpy as np

with open("inputs/day18.txt") as f: 
    lines = f.read().strip().split("\n")

filled = set()
for line in lines:
    x, y, z = map(int, line.split(","))
    filled.add((x, y, z))

surface_area = 0
for x, y, z in filled: 
    covered = 0

    position = np.array((x, y, z))
    for coordinate in range(3):
        positive_droplet = np.array([0, 0, 0])
        positive_droplet[coordinate] = 1

        negative_droplet = np.array([0, 0, 0])
        negative_droplet[coordinate] = -1

        covered += tuple(positive_droplet + position) in filled
        covered += tuple(negative_droplet + position) in filled
    surface_area += 6 - covered

print("DAY 18. - Part one")
print(f"THE ANSWER: The surface area of your scanned lava droplet is: {surface_area}")
