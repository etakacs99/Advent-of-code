class Coordinate: 
    x: int
    y: int

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, direction) -> 'Coordinate':
        new_coordinate = Coordinate(self.x, self.y)
        if direction == 'R':
            new_coordinate.x = new_coordinate.x + 1
        if direction == 'L':
            new_coordinate.x = new_coordinate.x - 1
        if direction == 'U':
            new_coordinate.y = new_coordinate.y + 1
        if direction == 'D':
            new_coordinate.y = new_coordinate.y - 1
        return new_coordinate

    def isNeighbour(self, other: 'Coordinate') -> bool: 
        return (abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1)

    def __str__(self) -> str:
        return (f"X: {self.x}, Y: {self.y}")

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y

    def __hash__(self) -> int:
        return hash(self.x) + hash(self.y)

    def calculateWay(self, other: 'Coordinate') -> 'Coordinate':
        new_coordinate = Coordinate(self.x, self.y)
        if self.x > other.x :  
            new_coordinate.x = new_coordinate.x - 1
        if self.x < other.x : 
            new_coordinate.x = new_coordinate.x + 1
        if self.y > other.y :  
            new_coordinate.y = new_coordinate.y - 1
        if self.y < other.y: 
            new_coordinate.y = new_coordinate.y + 1
        return new_coordinate

def main():
    #Part one
    file1 = open("inputs/day9.txt", "r")
    head = Coordinate(0, 0)
    tail = Coordinate(0, 0)
    used_coordinates = set()

    for movement in file1: 
        direction = movement.strip().split(" ")
        for i in range(int(direction[1])):
            head = head.move(direction[0])
            if not head.isNeighbour(tail): 
                tail = tail.calculateWay(head)
            used_coordinates.add(tail) 
    file1.close()

    print("DAY 9. - Part one")
    print(f"THE ANSWER: {len(used_coordinates)} positions visits the tail of the rope at least once.")

    #Part Two
    file2 = open("inputs/day9.txt", "r")
    knots = [Coordinate(0, 0) for _ in range(10)]
    used_coordinates = set()
   
    for movement in file2: 
        direction = movement.strip().split(" ")
        for i in range(int(direction[1])):
            knots[0] = knots[0].move(direction[0])
            for j in range(1, len(knots)): 
                if not knots[j - 1].isNeighbour(knots[j]): 
                    knots[j] = knots[j].calculateWay(knots[j - 1])
            used_coordinates.add(knots[-1]) 
    file2.close()

    print("DAY 9. - Part two")
    print(f"THE ANSWER: (larger rope with ten knots) {len(used_coordinates)} positions visits the tail of the rope at least once.")

if __name__ == "__main__":
    main()