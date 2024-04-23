#for loop
#for index in range(0, 4):
    #word = input('Give me a word: ')
    #first_last = word[0] + word[-1]
    #print("Here's the first and last letter: " + first_last)

#ifsloop combinations
text = input('Type your text here: ')
uppercase_count = 0
lowercase_count = 0
for index in range(0, len(text)):
    char = text[index]
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
print("Number of upper-case letter : ", uppercase_count)
print("Number of lower-case letter : ", lowercase_count)

#habis dibagi 7
start = int(input('Masukkan angka: '))
end = int(input('Sampai:'))
divide = int(input('Bilangan Yang Membagi: '))
number = start
while number <= end:
    if number % divide == 0:
        print(number, 'adalah bilangan yang habis dibagi', divide)
    number += 1

