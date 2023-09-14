"""import math

ip = list(map(int, input("Введите IP-адрес: ").split('.')))
mask = list(map(int, input("Введите маску: ").split('.')))

ip_bin = [format(i, "b") for i in ip]
mask_bin = [format(i, "b") for i in mask]

print(ip_bin, mask_bin)"""
import math


def prettyprint(array, columns, separators='  ', firstnumber=0):
    if firstnumber == 0:
        lines = math.ceil(len(array)-1 / columns)
    else:
        lines = math.ceil(len(array) / columns)

    diff = len(array) // columns
    for _ in range(lines):
        for __ in range(columns):
            if masks[_ + __*diff][0] < 10:
                print(' ', end='')
            print(*masks[_ + __*diff], sep=' - ', end='')
            if __ != columns-1:
                print(separators, end='')
        print()


masks = [
    [0, "000.000.000.000"], [1, "128.000.000.000"], [2, "192.000.000.000"],
    [3, "224.000.000.000"], [4, "240.000.000.000"], [5, "248.000.000.000"],
    [6, "252.000.000.000"], [7, "254.000.000.000"], [8, "255.000.000.000"],
    [9, "255.128.000.000"], [10, "255.192.000.000"], [11, "255.224.000.000"],
    [12, "255.240.000.000"], [13, "255.248.000.000"], [14, "255.252.000.000"],
    [15, "255.254.000.000"], [16, "255.255.000.000"], [17, "255.255.128.000"],
    [18, "255.255.192.000"], [19, "255.255.224.000"], [20, "255.255.240.000"],
    [21, "255.255.248.000"], [22, "255.255.252.000"], [23, "255.255.254.000"],
    [24, "255.255.255.000"], [25, "255.255.255.128"], [26, "255.255.255.192"],
    [27, "255.255.255.224"], [28, "255.255.255.240"], [29, "255.255.255.248"],
    [30, "255.255.255.252"], [31, "255.255.255.254"], [32, "255.255.255.255"]
]

prettyprint(masks, 3, separators=' | ')

'''
for i in range(0, len(masks), 3):
    for j in range(0, 3):
        print(*masks[i+j], sep=" - ", end="")
        if masks[i+j][0] == 32:
            print('.', end='')
        else:
            print(';  ', end='')
    print()
'''
