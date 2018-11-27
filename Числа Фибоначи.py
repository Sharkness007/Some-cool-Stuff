n = int(input("Enter n: "))
def F(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    else:
        return F(n-1) + F(n-2)
for i in range(0, n):
    print(F(i))
#Доработай так, чтобы сразу числа выводились