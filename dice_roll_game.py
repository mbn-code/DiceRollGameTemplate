import time
import random
# Roll the dice and see what you get, then wait for the ai to roll a dice and see who wins

print("""
Welcome to dice roll. You are playing against indi AI.
""")
time.sleep(2)

while 1:
    Roll_dice = input("Please roll the dice (roll/exit): ") 

    if Roll_dice.lower() == "roll":
        print("\n\n\nrolling dice. . .")
        time.sleep(random.randint(0,3))
        player_dice_roll = random.randint(1,6)
        print("\nYou rolled a " + str(player_dice_roll))

        print("\nNow indi AI is rolling. . .")
        time.sleep(random.randint(0,4))
        
        ai_dice_roll = random.randint(1,6)
        if ai_dice_roll > player_dice_roll:
            print("\nThe AI rolled " + str(ai_dice_roll) + " which is higher then your roll which was " + str(player_dice_roll))
            time.sleep(2)
            print("\nYou lost. . .\n\n")
        elif ai_dice_roll < player_dice_roll:
            print("The AI rolled " + str(ai_dice_roll) + " Which is lower then your roll which was " + str(player_dice_roll))
            time.sleep(1)
            print("You won!!\n\n\n")

    elif Roll_dice.lower() == "exit":
        exit()
    elif Roll_dice != "roll":
        print("please enter either 'roll' or 'exit'")
    elif Roll_dice != "exit":
        print("please enter either 'roll' or 'exit'")