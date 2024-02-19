from cs50 import get_int
import re

#Same as credit.py except using re module to validate start of card number

card = get_int("Number: ")

def luhn_checksum(card):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

length = 0
visa = card
mastercard = card
amex = card

length = len(str(card))

while visa >= 10:
    visa = int(visa / 10)

while mastercard >= 10**14:
    mastercard = int(mastercard / 10**14)

while amex >= 10**13:
    amex = int(amex / 10**13)

#check card is valid according to luhns algorithm

if luhn_checksum(card) == 0:
    if re.match(r"^4", visa) and (length == 13 or length == 16):
        print("VISA")
    elif length == 16 and re.match(r"(51|52|53|54|55)", mastercard):
        print("MASTERCARD")
    elif length == 15 and re.match(r"34|37)", amex):
        print("AMEX")
    else:
        print("INVALID")
else:
    print("INVALID")
