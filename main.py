from player import Player
from game import round_one, round_two, round_three

def main():
    print("Welcome to Number Duel!")
    
    p1 = Player("Player 1")
    p2 = Player("Player 2")

    p1.choose_order()
    p2.choose_order()

    results = [
        round_one(p1, p2),
        round_two(p1, p2),
        round_three(p1, p2)
    ]

    p1_score = results.count(1)
    p2_score = results.count(-1)

    print(f"\nPlayer 1 won {p1_score} rounds.")
    print(f"Player 2 won {p2_score} rounds.")
    

    if p1_score > p2_score:
        print("Congratulations! Player 1 wins the duel!")
    elif p1_score < p2_score:
        print("Congratulations! Player 2 wins the duel!")
    else:
        print("peace! It's a tie!")

if __name__ == "__main__":
    main()
