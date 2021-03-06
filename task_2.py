"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""


x = [345,567,324,546456,3095438,4356]


def find_min(sequence):   #Квадратичная сложность
    elements = set(sequence)
    for elem in elements:
        lesser_elements_count = 0
        for curr_elem in elements:
            if elem < curr_elem:
                lesser_elements_count += 1
        if lesser_elements_count == len(elements) - 1:
            return elem
print(find_min(x))



def my_min(sequence): #Линейная сложность
    low = sequence[0]
    for i in sequence:
        if i < low:
            low = i
    return low
print (my_min(x))