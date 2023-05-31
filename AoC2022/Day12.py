from collections import deque

class Point:
    x: int 
    y: int 

    def __init__(self, x, y) -> 'Point':
        self.x = x
        self.y = y
   
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(tuple((self.x, self.y)))

    def neighbours(self) -> list['Point']:
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        neighbours = set()
        for dx, dy in DIRS:
            next_x = self.x + dx
            next_y = self.y + dy
            neighbours.add(Point(next_x, next_y))
        return neighbours

    def __str__(self):
        return (f"X: {self.x}, Y: {self.y}")
            
def bfs(start:'Point', end:'Point', board) -> int:
    horizon = deque([(start, 0)])
    seen = set()
    while horizon: 
        p, depth = horizon.popleft()
        if p in seen: 
            continue
        elif p == end:
            return depth

        seen.add(p)

        for n in p.neighbours():
            if n not in board: 
                continue
            #Find next ASCII char.(If the neighbour is that char the depth grow and we need to inspect the neighbour.)
            if ord(board[n])-1 <= ord(board[p]):
                horizon.append((n, depth + 1))
    
    return 1e9

def main():
    #Parse input.
    file = open("inputs/day12.txt", "r")
    board = {}
    for y, line in enumerate(file):
        for x,c in enumerate(line.strip()):
            board[Point(x,y)] = c 
            if c == 'S':
                start = Point(x,y)
                board[start] = 'a'
            elif c == 'E': 
                end = Point(x,y)
                board[end] = 'z'
    file.close()

    #for x in board: 
    #    print(x, board[x])
    print("DAY 12. - Part one")
    print(f"THE ANSWER: The fewest steps required to move from your current position to the location that should get the best signal is {bfs(start, end, board)}.")

    print("DAY 12. - Part two")
    print(f"THE ANSWER: The fewest steps required to move starting from any square with elevation a to the location that should get the best signal is { min(bfs(s, end, board) for s in board if board[s] == 'a')}.")

if __name__ == "__main__":
    main()