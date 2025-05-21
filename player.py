import random

class Player:
    def __init__(self, name):
        self.name = name
        self.numbers = random.choices(range(1, 10), k=6)
        self.order = []

    def choose_order(self):
        print(f"\n{self.name}, your numbers are: {self.numbers}")
        used = []

        # Round 1: 
        i = input("Enter the index for your first number (0-5): ")
        while not i.isdigit() or int(i) not in range(6) or int(i) in used:
            i = input("Invalid. Enter a new index (0-5): ")
        used.append(int(i))

        # Round 2:
        while True:
            two = input("Enter two more indices (space separated): ").split()
            if len(two) != 2:
                print("Please enter exactly two indices.")
                continue
            a, b = two
            if a.isdigit() and b.isdigit():
                a = int(a)
                b = int(b)
                if a in range(6) and b in range(6) and a not in used and b not in used:
                    used.append(a)
                    used.append(b)
                    break
            print("Invalid input. Try again.")

        # Round 3: 
        while True:
            three = input("Enter the last three indices (space separated): ").split()
            if len(three) != 3:
                print("Please enter exactly three indices.")
                continue
            x, y, z = three
            if x.isdigit() and y.isdigit() and z.isdigit():
                x = int(x)
                y = int(y)
                z = int(z)
                if all(k in range(6) and k not in used for k in [x, y, z]):
                    used += [x, y, z]
                    break
            print("Invalid input. Try again.")

        # 生成最终顺序
        self.order = [self.numbers[i] for i in used]
