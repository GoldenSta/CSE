import random
current_money = 15
playing = True
total_roles = 0
top_money = 15
top_roles = 0

while current_money > 0 and playing:
    dice_roll1 = random.randint(1, 6)
    dice_roll12 = random.randint(1, 6)
    print(dice_roll1, dice_roll12)
    role = dice_roll1 + dice_roll12
    if role == 7:
        current_money += 4
        print("Rolled a 7.")
        total_roles += 1
        top_money += 4
        top_roles += 1
        if current_money > top_money:
            current_money = top_money
            total_roles = top_roles
    else:
        current_money -= 1
        print("Roll Again.")
        total_roles += 1

print("Game Over. You took %d rounds" % total_roles)
print("You lose %r dollars" % top_money)
