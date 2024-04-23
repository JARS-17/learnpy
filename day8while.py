#exercise
pyramid_size = int(input("Pyramid size: "))
index = 1
while index <= pyramid_size:
    spacing = pyramid_size - index
    print(" " * spacing + "#" * (index * 2))
    index += 1

#while bersarang
sentence = 'Aku adalah seorang mahasiswa sains data.'
position = 0
while position < len(sentence)-10:
    index = position
    while index < position+10:
        print(sentence[index], end='')
        index += 1
    print()
    position += 1



