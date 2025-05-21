def compare(val1, val2):
    if val1 > val2:
        return 1
    elif val1 < val2:
        return -1
    else:
        return 0

def round_one(p1, p2):
    print("\n====== Round 1 ======")
    print(f"{p1.name}: {p1.order[0]}")
    print(f"{p2.name}: {p2.order[0]}")
    result = compare(p1.order[0], p2.order[0])
    show_winner(result, p1, p2)
    return result

def round_two(p1, p2):
    print("\n====== Round 2 ======")
    sum1 = p1.order[1] + p1.order[2]
    sum2 = p2.order[1] + p2.order[2]
    print(f"{p1.name}: {sum1 % 10}")
    print(f"{p2.name}: {sum2 % 10}")
    result = compare(sum1 % 10, sum2 % 10)
    show_winner(result, p1, p2)
    return result

def round_three(p1, p2):
    print("\n====== Round 3 ======")
    prod1 = p1.order[3] * p1.order[4] * p1.order[5]
    prod2 = p2.order[3] * p2.order[4] * p2.order[5]
    print(f"{p1.name}: {prod1}")
    print(f"{p2.name}: {prod2}")
    result = compare(prod1, prod2)
    show_winner(result, p1, p2)
    return result

def show_winner(result, p1, p2):
    if result == 1:
        print(f"{p1.name} wins this round!")
    elif result == -1:
        print(f"{p2.name} wins this round!")
    else:
        print("This round is a tie.")
