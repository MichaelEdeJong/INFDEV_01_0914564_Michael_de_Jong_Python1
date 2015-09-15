size = input("Size of the block: ")
triangle = int(0)

for x in range(0, int(size)):
    if triangle > 0 and triangle < int(size) -1:
        print('*' * (int(size) - triangle) + ' ' * triangle + '*')
    else:
        print('*' * (int(size) + 1))
    triangle = triangle + int(1);