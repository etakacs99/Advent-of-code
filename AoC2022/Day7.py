class File:
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

    def printFile(self, indent:int):
        for i in range(0, indent):
            print(" ", end="")
        print(f"- {self.name} (file, size={self.size})")

class Directory:

    list_of_dirs: list['Directory']
    list_of_files: list['File']

    def __init__(self, name: str, parent: 'Directory'):
        self.name = name
        self.parent = parent
        self.list_of_dirs = []
        self.list_of_files = []

    def printDir(self, indent: str):
        for i in range(0, indent):
            print(" ", end="")
        print(f"- {self.name} (dir)")
        for dir in self.list_of_dirs:
            dir.printDir(indent + 2) 
        for file in self.list_of_files:
            file.printFile(indent + 2)

    def calculateSize(self, list_of_dir_size: list[int]) -> int :
        size = 0
        for dir in self.list_of_dirs:
            size = size + dir.calculateSize(list_of_dir_size)
        for file in self.list_of_files:
            size = size + file.size
        if size <= 100000:
            list_of_dir_size.append(size)
        return size

    def calculateSmallestDir(self, list_of_dir_size: list[int]) -> int :
        size = 0
        for dir in self.list_of_dirs:
            size = size + dir.calculateSmallestDir(list_of_dir_size)
        for file in self.list_of_files:
            size = size + file.size
        list_of_dir_size.append(size)
        return size

def main():
    file = open("inputs/day7.txt", "r")
    root = Directory("/", None)
    current_dir = root
    
    for line in file: 
        if line.startswith("$"):
            processed_line = line.strip().split(" ")
            if processed_line[1] == "cd":
                if processed_line[2] == "/":
                    current_dir = root
                elif processed_line[2] == "..":
                    current_dir = current_dir.parent
                else:
                    #assumption: the input must be always correct 
                    for d in current_dir.list_of_dirs:
                        if d.name == processed_line[2]:
                            current_dir = d
                            break
            elif processed_line[1] == "ls":
                pass
        else:
            processed_line = line.strip().split(" ")
            if processed_line[0] == "dir":
                new_dir = Directory(processed_line[1], current_dir)
                current_dir.list_of_dirs.append(new_dir)
            else:
                new_file = File(processed_line[1], int(processed_line[0]))
                current_dir.list_of_files.append(new_file)
    file.close() 

    #root.printDir(0)
    list_of_sums = []
    root.calculateSize(list_of_sums)
    result1 = 0
    for sum in list_of_sums: 
        result1 = result1 + sum

    print("DAY 7. - Part one")
    print("THE ANSWER: The sum of the total sizes of those directories is: " + str(result1))

    list_of_all_dir_size = []
    root_size = root.calculateSmallestDir(list_of_all_dir_size)
    available_size = 70000000 - root_size
    min = None
    for dir_size in list_of_all_dir_size:
        if available_size + dir_size >= 30000000:
            if min == None or min >= dir_size: 
                min = dir_size

    print("DAY 7. - Part two")
    print("THE ANSWER: The total size of that directory is: " + str(min))

if __name__ == "__main__":
    main()