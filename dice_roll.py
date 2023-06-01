import random

def roll_dice():
    min_value = 1
    max_value = 6
    return random.randint(min_value,max_value)

def simulating_dice_roll(num_rolls):
    print(f"simulate {num_rolls} dice rolls")
    for _ in range(num_rolls):
        dice_roll = roll_dice()
        print("Dice rolled:", dice_roll)

num_rolls = int(input("Enter the number of times u want to roll the dice: "))
simulating_dice_roll(num_rolls)


