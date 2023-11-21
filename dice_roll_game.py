import time
import random

def roll_dice():
    return random.randint(1, 6)

def print_dice_roll(player, value):
    print(f"\n{player} rolled a {value}")

def print_round_result(player, player_value, ai_value, result):
    print(f"\n{player} rolled {player_value} | AI rolled {ai_value}")
    time.sleep(1)
    print(result)

def print_score(player_wins, ai_wins):
    print(f"\nCurrent Score - You: {player_wins} | AI: {ai_wins}")

def main():
    print("Welcome to Dice Roll. You are playing against indi AI.")
    time.sleep(2)

    player_wins = 0
    ai_wins = 0
    rounds = 1

    while True:
        print(f"\nRound {rounds}")
        player_input = input("Please roll the dice (roll/exit): ")

        if player_input.lower() == "roll":
            print("\nRolling dice...")
            time.sleep(random.randint(1, 3))

            player_dice = roll_dice()
            print_dice_roll("You", player_dice)

            print("\nNow indi AI is rolling...")
            time.sleep(random.randint(1, 4))

            ai_dice = roll_dice()
            print_dice_roll("AI", ai_dice)

            if ai_dice > player_dice:
                print_round_result("You", player_dice, ai_dice, "You lost.\n")
                ai_wins += 1
            elif ai_dice < player_dice:
                print_round_result("You", player_dice, ai_dice, "You won!\n")
                player_wins += 1
            else:
                print("\nIt's a tie!\n")

            print_score(player_wins, ai_wins)
            rounds += 1

        elif player_input.lower() == "exit":
            print("\nThanks for playing!")
            exit()

        else:
            print("Please enter either 'roll' or 'exit'")

if __name__ == "__main__":
    main()
