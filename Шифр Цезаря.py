import string
key2 = string.ascii_lowercase
key2 += string.ascii_uppercase
key1 = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
key1 += key1.upper()
key3 = "    ....,,,,!!!!????(((())))::::----"
key = key1 + key2 + key3
#key1 33 + 33 букв; key2 26 + 26 букв
#key3 27 символов
#key 145 символов

while True:
    try:
        s = str()
        user_input = input("Введите фразу (rus, eng), я её зашифрую шифром Цезаря: ")
        for i in user_input:
            if key.index(i) < 33:
                if key.index(i) + 3 > 32:
                    s += key[key.index(i) + 3 - 33]
                else:
                    s += key[key.index(i) + 3]
            elif key.index(i) < 66:
                if key.index(i) + 3 > 65:
                    s += key[key.index(i) + 3 - 33]
                else:
                    s += key[key.index(i) + 3]
            elif key.index(i) < 92:
                if key.index(i) + 3 > 91:
                    s += key[key.index(i) + 3 - 26]
                else:
                    s += key[key.index(i) + 3]
            elif key.index(i) < 118:
                if key.index(i) + 3 > 117:
                    s += key[key.index(i) + 3 - 26]
                else:
                    s += key[key.index(i) + 3]
            else:
                s += key[key.index(i) + 3]
        print(s)
    except:
            print("Ну, лучше не вводи числа и замудрённые символы))")
