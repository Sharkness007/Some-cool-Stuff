#ord - превращает знак в номер кода Unicode
#chr - декодирует номер Unicode в знак
#print(ord("H")) #72
#print(chr(72))  #H
#Hackerrank сайтик интересный


# def representation(array, delimiter="") -> str:
#     result = str()
#     for i in array:
#         result += i
#         result += delimiter  #если не вводить delimiter, то значение по умолчанию ""
#     return result
# print(representation(["hello", "world"], delimiter=","))


# def zero(num):
#     num = num - (num if num > 0 else -num)
#     return num
# print(zero(20))
# print(zero(-20))
# print(open.__doc__) #посмотреть документацию функции open



# file = open("test.txt", "a")  #"a" от слова append. Открывает файл, не стирая содержимое
# file.write("def f(a, b):\n  a,b = b,a")
# file.close()

# with open("test.txt", "a") as file:
#     file.write("def f(a, b):\n  a,b = b,a")

# with open("test.txt", "r") as file:
#     count = 0
#     for line in file:
#         count += 1
#         print(count, line)
#         if '(' in line:
#             print("Мы нашли (!")
##############################################################
# def set_value(key: str, value: str) -> None:
#
#
#     with open("example.db", "a") as file:
#         file.write(key + ":" + value + "\n")
##############################################################
#
# set_value("name", "Alex")
# set_value("name1", "Alice")
# set_value("our_sun", "SUN")
#
#########################################################
# def find(key):
#
#
#     count = 0
#     with open("example.db", "r") as file:
#         for line in file:
#             if key in line:
#                 count += 1
#         if count > 0:
#             print("Слово " + key + " найдено", count, "раз")
#         else:
#             print("Слово " + key + " НЕ найдено")
#
##################################################################
# find("Alex")
##################################################################
# def get_value(key):
#
#
#     key += ":"
#     with open("example.db", "r") as file:
#         for line in file:
#             if key in line:
#                 #return line[line.index(":")+1:-1]
#                 return line.split(":")[1].replace("\n", "")
#
##################################################################
# print(get_value("name"))

# def set_value(key, value):        #Добавляет в файл строку "ключ:значение"
#
#     with open("example.db", "a") as file:
#         file.write(f"{key}:{value}\n")
#
# set_value("name", "Sergey")

# ###################################################################################################################################
# def add_value(key, value):
#
#
#     with open("example.db", "r") as file:
#         for line in file:
#             if key + ":" in line:    #Проверяем, существует ли уже ключ
#                 raise "KeyError" ("You can't use the same key many times!") #Если да - вызываем исключение
#     with open("example.db", "a") as file:
#         file.write(f"{key}:{value}\n")   #Если исключение не вызвалось - всё в порядке, добавляем
# ###################################################################################################################################
#
# add_value("name2", "Anton")

def modify_value(key, value):


    with open("example.db", "a") as file:
        file.write(f"{key}:{value}\n")


#modify_value("name2", "Kenny")

def get_value(key):


    with open("example.db", "r") as file:
        for line in file:
            if key + ":" in line:
                result = line
        return result.split(":")[1].replace("\n", "")





