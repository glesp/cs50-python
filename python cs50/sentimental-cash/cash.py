from cs50 import get_float

change = get_float("Change: ")
change = change * 100

coins = 0;

while(change > 0):
    while change >= 25:
        change = change - 25
        coins += 1

    while change >= 10:
        change = change - 10
        coins += 1

    while change >= 5:
        change = change - 5
        coins += 1

    while change >= 1:
        change = change - 1
        coins += 1

print(coins)

