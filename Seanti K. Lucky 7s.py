import random
money = 15
playing = True
total_roles = 0
Top_money = 15
Top_roles = 0

while money > 0 and playing:
    dice_roll1 = random.randint(1, 6)
    dice_roll12 = random.randint(1, 6)
    print(dice_roll1, dice_roll12)
    role = dice_roll1 + dice_roll12
    if role == 7:
        money += 5
    print("Rolled a 7.")
    total_roles += 1
    top_money += 5
    Top_round += 1
