import random

top_of_range = input("type a number")
if top_of_range.isdigit():
    top_of_range == int (top_of_range)
    if top_of_range <= 0:
        print("Pleas type a number larger than 0")
        quit()
    else:
        print("Pleas type a number larger next time")
random_number = random.randint(0, 100)
print(random_number)