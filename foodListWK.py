from fancyFoodWK import fancyFood

foodList = []
numFood = 0
while True:
    try:
        numFood = int(input("How many items will you order today "))
    except ValueError:
        print("Please enter a valid amount.")
        continue
    if numFood > 0:
        pass
    else:
        print("You must order at least 1 item.")
print(numFood)
