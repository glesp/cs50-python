from cs50 import get_int


while True:
    height = get_int("Height: ")
    if height > 0 and height < 9:
        break
    else:
        print("please enter height between 1 and 8")

for i in range(1, height + 1):
    print(" " * (height - i) + "#" * i)


