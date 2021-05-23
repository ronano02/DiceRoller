import random

error = 0
exit = 0
while error == 0:
    dice = int(input("Enter size of die: "))
    if dice >= 3:
        error = 1
    if dice < 3:
        print("Size is too small, dice have atleast 3 sides")

print("Type \'Roll' to simulate the dice roll")
print("Type \'Done' when finished")

while exit == 0:
    roll = input()
    if roll in {'Done', 'done', 'DONE'}:
        exit = 1
    elif roll in {'roll', 'ROLL', 'Roll'}:
        print(random.randrange(1, dice))
    else:
        print("Invalid Entry")



