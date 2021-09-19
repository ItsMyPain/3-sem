def Mnogobonachi(n):
    if 1 <= n <= 8:
        return 0
    elif n == 9:
        return 1
    elif n > 9:
        return Mnogobonachi(n - 1) + Mnogobonachi(n - 2) + Mnogobonachi(n - 3) + Mnogobonachi(n - 4) + Mnogobonachi(n - 5) + Mnogobonachi(n - 6) + Mnogobonachi(n - 7) + Mnogobonachi(n - 8) + Mnogobonachi(n - 9)
print(Mnogobonachi(int(input())))