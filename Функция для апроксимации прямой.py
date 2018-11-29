def аппроксимация(x, y, что_вывести_A_C_dA_dC_return_info):  #Обязательно нужно ввести
                                                             # список/кортеж длинной > 2

    from math import sqrt

    x_среднее = 0
    y_среднее = 0
    D = 0       #Средний квадрат отклонения иксов
    A = 0       #Угловой коэффициент Y = AX + C
    C = 0       #Коэффициент "смещения", слагаемое
    E = 0       #Понятия не имею как описать, вспомогательная переменная
    dA = 0      #Погрешность для А
    dC = 0      #Погрешность для C

    for i in x:
        x_среднее += i
    x_среднее /= len(x)

    for i in y:
        y_среднее += i
    y_среднее /= len(y)

    for i in x:
        D += (i - x_среднее)**2

    for i in range(len(x)):
        A += (x[i] - x_среднее)*y[i]
    A /= D

    C = y_среднее - A * x_среднее

    for i in range(len(x)):
        E += (y[i] - A*x[i] - C)**2
    E /= (len(x)-2)

    dA = sqrt(E/D)

    dC = sqrt((1/len(x) + x_среднее**2/D)*E)

    if что_вывести_A_C_dA_dC_return_info == "A":
        return A
    if что_вывести_A_C_dA_dC_return_info == "C":
        return C
    if что_вывести_A_C_dA_dC_return_info == "info":
        print("A =", A, "+-", dA)
        print("C =", C, "+-", dC)
    if что_вывести_A_C_dA_dC_return_info == "dA":
        return dA
    if что_вывести_A_C_dA_dC_return_info == "dC":
        return dC


a = [аппроксимация([1,3,5,7,9], [1,3,4,5,9], "info")]
print(a)
