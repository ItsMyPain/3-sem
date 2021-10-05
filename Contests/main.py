input1 = input().split('0')
out = sorted(input1, key=len, reverse=True)
print(out)