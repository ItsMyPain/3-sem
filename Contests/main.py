input1 = input()
fin = input()
try:
    f = open(input1, 'r')
    print(f.read().lower().split().count(fin.lower()))
except FileNotFoundError:
    print(0)

##
