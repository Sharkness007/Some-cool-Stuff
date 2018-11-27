zero = float(input("Чему равно значение в нуле?: "))
base = float(input("На каком сантиметре ты знаешь точное значение?: "))
b = (float(input("Чему равно значение на " + str(base) + "-ом см?: ")) - zero) / base

while True:
    try:
        a = (float(input("Значение величины?: ")) - zero) / b
        print("Отложи " + str(a) + " см")
    except:
        continue
