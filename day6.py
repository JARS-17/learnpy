# Write your code here :-)
height = int(input('Height in cm: '))
if height >= 40 and height <= 70:
    print('You may ride')
if height < 40 or height > 70:
    print('You may not ride')

#else
# name = input("What is your first name? ")
#if len(name) < 35 and name[0].isupper():
#   print("Thats a valid name")
#else:
#    print("Sorry, your name is either")
#    print("  * Too long")

experience = input("What level of Spanish experience do you have? ")

if experience == "none":
    print("You should take Spanish 101")
elif experience == "101":
    print("You should take Spanish 102")
elif experience == "102":
    print("You should take Spanish 201")
elif experience == "201":
    print("You should take Spanish 202")
elif experience == "202":
    print("You should move on to more advanced classes!")
else:
    print("Sorry, I didn't recognize what you entered.")
    print("Please give me one of these experience levels: none, 101, 102, 201, or 202.")

