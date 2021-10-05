def toFixed(f: float, n = 0):
    a, b = str(f).split('.')
    return '{}.{}{}'.format(a, b[:n], '0'*(n-len(b)))

number = input()
ex = number.find('.')
if ex == -1:
    print(int(number) - 1)
else:
    new1 = (int(float(number) * 10 ** (len(number) - ex - 1)) - 1) / 10 ** (len(number) - ex - 1)
    print(toFixed(new1, len(number) - ex - 1))
