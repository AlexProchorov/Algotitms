"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


d ={
    'Nokia':3500,
    'Motorolla':4240,
    'Simens': 5234,
    'Iphone': 9845
}
# 1 вариант решения

sorted_values = sorted(d.values(), reverse=True) #O(n log n) - линейно-логарифмическая
print(sorted_values)
sorted_rating = {}
iterator = 0
for i in sorted_values: #O(n) - линейная
    for k in d.keys(): #O(n) - линейная
        if d[k] == i and iterator < 3:
            sorted_rating[k] = d[k]
            iterator += 1
            break
print (sorted_rating)
#Сложность O(n^2) - квадратичная.



# 2 вариант решения

from collections import Counter
print(Counter(d).most_common(3))
# Линейная сложность, самое эффективное и быстрое в написании, импорт библиотек.


