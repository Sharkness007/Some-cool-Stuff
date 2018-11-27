from builtins import ZeroDivisionError

print("Это калькулятор")
while True:
	try:
		a = float(input("Введите первое число: "))
		s = input('Введите любую из этих операций "*", "+", "-", "/": ')
		d = float(input("Введите второе число: "))
	except ValueError:
		print("Кажется я просил ввести ЧИСЛО?")
		continue
	try:
		if s == "+":
			print(str(a+d))
		elif s == "-":
			print(str(a-d))
		elif s == "*":
			print(str(a*d))
		elif s == "/":
			print(str(a/d))
		else:
			print("Я не знаю такой операции!")
	except ZeroDivisionError:
		print("Нельзя делить на ноль!")
		continue