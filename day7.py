hungry = input('Are you hungry?: ')

if hungry == "yes":
    hungry_yes = input("That's bad. What do you want to eat?: ")
    if hungry_yes == "pizza" :
        print("Go to  Pizza hut")
    elif hungry_yes == "burger":
            print ("Go to Burger King")
    elif hungry_yes == "salad":
            print("Go to home and make salad")
else : print("Unsure")

thirsty = input("Are you thirsty? ")
if thirsty == "yes":
    thirsty_yes = input("What do you want to drink?: ")
    if thirsty_yes == "water":
        print("This is your water")
    elif thirty_yes == "juice":
        print("This is your juice")
else : print("Keep working")
