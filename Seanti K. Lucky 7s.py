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
        money += 4
        print("Rolled a 7.")
        total_roles += 1
        Top_money += 4
        Top_roles += 1
        if money > Top_money:
            money = Top_money
    else:
        money -= 1
        print("Roll Again.")
        total_roles += 1

print("You took %d rounds" % total_roles)
print("You have %r money" % Top_money)
