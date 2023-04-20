"""A simple credit card validator.
A program being able to determine whether a given card number is valid or not."""

card_number = list(input("Enter a card number:   ").replace(" ", ""))

card_number = [int(digit) for digit in card_number]

checking_digit = card_number.pop()

card_number.reverse()

card_number_x_2 = []

for counter, digit in enumerate(card_number):
    if (counter % 2 == 0) and (digit * 2 > 9):
        double_digit = digit * 2 - 9
        card_number_x_2.append(double_digit)
    elif counter % 2 == 0:
        double_digit = digit * 2
        card_number_x_2.append(double_digit)
    else:
        card_number_x_2.append(digit)

digits_addition = sum(card_number_x_2) + checking_digit

if digits_addition % 10 == 0:
    print("Your credit card is valid")
else:
    print("Sorry !!! This credit card isn't valid")
