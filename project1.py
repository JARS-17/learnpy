#fungsi bendera USA

width = int(input('Flag width: '))
height = int(input('Flag height: '))

w1 = int(width/2)
h1 = int(height/2)

case1 = "#" * w1 + "-" * w1 + '\n'
case2 = "-" * width + '\n'
print(case1 * h1 ,end='')
print(case2 * h1 ,end='')
