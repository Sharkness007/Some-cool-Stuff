def check(array):                      #Проверка "Отсортирован ли массив или нет"
    counter = 0
    for i in range(len(array)-1):
        if array[i] <= array[i+1]:
            counter += 1
    if counter + 1 == len(array):
        return True
    else:
        return False

def quickSort(array):
    while not check(array):
        for i in array:
            for k in array:
                if i < k and array.index(i) > array.index(k): #Если число (i) меньше другого числа (k)
                    array.remove(k)                           #И при этом индекс числа (i) больше
                    array.append(k)                           #индекса числа (k), значит число (к)Нужно отправить в конец списка [5, 4, 9, 7, "6"] --> [5, 4, "6", 9, 7] В данном случае число (i) это "6"
                if i > k and array.index(i) < array.index(k): #Почти то же самое, только число отправляется в начало списка
                    array.remove(k)
                    array.insert(0, k)
                if i == k and array.count(i) != 1:            #Если числа одинаковые, то они идут друг за другом
                    array.remove(k)
                    array.insert(array.index(i)+1, i)
                print(array)
    return array

s = [1, 3, 10, 4, 6, 9, 13, 20, 123, 8293, 0, 92, 9, 15,6]
print(quickSort(s))
