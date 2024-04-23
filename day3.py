# lesson 1 output bilangan bulat
name = "Pierre"
email = "pierre@gmail.com"
age = 50
height = 72
print("His name is " + name)
print(name + " can be contacted at " + email)
print("He is " + str(age) + " years old and is " + str(height) + " inches tall")

# lesson 2 penggaplikasian
revenue = int(input("The Bussines revenue: "))
cost = int(input("The Bussines cost: "))
profit = revenue - cost
print("The Bussines Profit: " + str(profit))
# cost_value = '#' * cost
# profit_value = '#' * profit
# perbaikan dengan pembatasan 25 digit
cost_value = "#" * int((cost / revenue) * 25)
profit_value = "#" * int((profit / revenue) * 25)
print("cost chart: " + cost_value)
print("profit chart: " + profit_value)

#lesson 3 indeks string
text = input('Your name: ')
last = text[len(text) - 1]
other = text [len(text) - 2]
print('Name your: ' + other + last)
