numbers = [int(i)for i in input().split()]
N = int(input())
print(*sorted(sorted(numbers, reverse=True)[0:N]), sep='\n')
