"""
Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции
2) определите сложность алгоритма в целом

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'
Не забудтье оценить итоговую сложность каждого из трех алгоритмов.

Примечание:
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.

    Алгоритм 3:
    Создать множество из списка

    Сложность: !!!.
    """
    lst_to_set = set(lst_obj)
    # Функция пробежит по всем значениям, отфильтрует по уникальным и вернет список уник. значений
    # Сложность зависит от длины, линейная сложность
    return lst_to_set  # Линейная сложность


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах

    Сложность: !!!.
    """
    for j in range(len(lst_obj)):          # Линейная сложность
        if lst_obj[j] in lst_obj[j+1:]:    # Зависит от длины списка, линейная
            return False                   # константная
    return True                            # константная


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.

    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.

    Сложность: !!!
    """
    lst_copy = list(lst_obj)                 # Зависит от длины списка, линейная
    lst_copy.sort()                          # Линейно-логарифмическая сложность
    for i in range(len(lst_obj) - 1):        # линейная
        if lst_copy[i] == lst_copy[i+1]:     # линейно, зависит от длины
            return False                     # линейная
    return True                              # Общая сложность - линейно логарифмическая

#############################################################################################


for j in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных   |
    # Я бы сказал линейно-логарифмическая сложность
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))
