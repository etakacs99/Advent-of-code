class Monkey:
    inspect_number: int
    items: list[int]
    test_division: int
    true_case: int
    false_case: int
    operation: str
    operation_number: int

    def __init__(self, items: list[int], test_division: int, true_case: int, false_case: int, operation: str, operation_number: int):
        self.items = items
        self.inspect_number = 0
        self.test_division = test_division
        self.true_case = true_case
        self.false_case = false_case
        self.operation = operation
        self.operation_number = operation_number

    def change_worry_level(self, old) -> int:
        number = self.operation_number
        if self.operation_number == None: 
            number = old
        if self.operation ==  '+':
            return old + number
        elif self.operation ==  '-':
            return old - number
        elif self.operation ==  '*':
            return old * number

def main():
    #Part one
    monkeys_part_one = [
        Monkey([74, 73, 57, 77, 74], 19, 6, 7, '*', 11), 
        Monkey([99, 77, 79], 2, 6, 0, '+', 8),
        Monkey([64, 67, 50, 96, 89, 82, 82], 3, 5, 3, '+', 1), 
        Monkey([88], 17, 5, 4, '*', 7),
        Monkey([80, 66, 98, 83, 70, 63, 57, 66], 13, 0, 1, '+', 4),
        Monkey([81, 93, 90, 61, 62, 64], 7, 1, 4, '+', 7), 
        Monkey([69, 97, 88, 93], 5, 7, 2, '*', None), 
        Monkey([59, 80], 11, 2, 3, '+', 6)]

    for round in range(20):
        for monkey in monkeys_part_one: 
            while len(monkey.items) != 0:
                item = monkey.items[0]
                worry = monkey.change_worry_level(item) // 3 
                if worry % monkey.test_division == 0:
                    monkeys_part_one[monkey.true_case].items.append(worry)
                else: 
                    monkeys_part_one[monkey.false_case].items.append(worry)
                monkey.inspect_number = monkey.inspect_number + 1
                monkey.items.pop(0)

    inspect_sums_part_one = []
    for i in monkeys_part_one:
        inspect_sums_part_one.append(i.inspect_number)
    inspect_sums_part_one.sort(reverse=True)

    print("DAY 11. - Part one")
    print(f"THE ANSWER: The level of monkey business after 20 rounds of stuff-slinging simian shenanigans is : {inspect_sums_part_one[0]* inspect_sums_part_one[1]}")

    #Part two
    monkeys_part_two = [
        Monkey([74, 73, 57, 77, 74], 19, 6, 7, '*', 11), 
        Monkey([99, 77, 79], 2, 6, 0, '+', 8),
        Monkey([64, 67, 50, 96, 89, 82, 82], 3, 5, 3, '+', 1), 
        Monkey([88], 17, 5, 4, '*', 7),
        Monkey([80, 66, 98, 83, 70, 63, 57, 66], 13, 0, 1, '+', 4),
        Monkey([81, 93, 90, 61, 62, 64], 7, 1, 4, '+', 7), 
        Monkey([69, 97, 88, 93], 5, 7, 2, '*', None), 
        Monkey([59, 80], 11, 2, 3, '+', 6)]
        
    monkey_divisor = 1
    for x in monkeys_part_two:
        monkey_divisor = monkey_divisor * x.test_division

    for round in range(10000):
        for monkey in monkeys_part_two: 
            while len(monkey.items) != 0:
                item = monkey.items[0]
                worry = monkey.change_worry_level(item) % monkey_divisor
                if worry % monkey.test_division == 0:
                    monkeys_part_two[monkey.true_case].items.append(worry)
                else: 
                    monkeys_part_two[monkey.false_case].items.append(worry)
                monkey.inspect_number = monkey.inspect_number + 1
                monkey.items.pop(0)

    inspect_sums_part_two = []
    for i in monkeys_part_two:
        inspect_sums_part_two.append(i.inspect_number)
    inspect_sums_part_two.sort(reverse=True)

    print("DAY 11. - Part two")
    print(f"THE ANSWER: The level of monkey business after 10000 rounds: {inspect_sums_part_two[0]* inspect_sums_part_two[1]}")

if __name__ =="__main__":
    main()