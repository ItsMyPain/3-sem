numbers = [int(i) for i in input().split() if i.lstrip('-+').isdigit()]
print(sum(numbers))
