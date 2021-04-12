from timeit import timeit
from memory_profiler import profile
from random import randint


def bubble_sort(nums):
    i = 1
    while i < len(nums):
        for j in range(len(nums) - i):
            if nums[j] < nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

        i += 1
    return nums


def upgrade_bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


random_list_of_nums = [randint(-100, 99) for _ in range(100)]
print(f'Исходный: {random_list_of_nums}')
print(f'Пузырек: {bubble_sort(random_list_of_nums[:])}')
print(f'Upgrade: {upgrade_bubble_sort(random_list_of_nums[:])}\n')


@profile
def bubble_sort_profile(list_obj):
    bubble_sort(list_obj)


@profile
def upgrade_bubble_sort_profile(list_obj):
    upgrade_bubble_sort(list_obj)


print('Профилировка памяти:')
print('Пузырек')
bubble_sort_profile(random_list_of_nums[:])

print('Upgrade')
upgrade_bubble_sort_profile(random_list_of_nums[:])

print('\nЗамеры времени:')
print(f"Пузырек: {timeit('bubble_sort(random_list_of_nums[:])', number=1000, globals=globals())}")
print(f"Upgrade: {timeit('upgrade_bubble_sort(random_list_of_nums[:])', number=1000, globals=globals())}")

'''
Профилировка памяти:
Пузырек
Filename: K:/Programming/algorithms/-algorithms_2021/Урок 7. Практическое задание/task_1.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    55     38.8 MiB     38.8 MiB           1   @profile
    56                                         def bubble_sort_profile(list_obj):
    57     38.9 MiB      0.0 MiB           1       bubble_sort(list_obj)
Upgrade
Filename: K:/Programming/algorithms/-algorithms_2021/Урок 7. Практическое задание/task_1.py
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    60     38.9 MiB     38.9 MiB           1   @profile
    61                                         def upgrade_bubble_sort_profile(list_obj):
    62     38.9 MiB      0.0 MiB           1       upgrade_bubble_sort(list_obj)
Замеры времени:
Пузырек: 0.875528627
Upgrade: 1.092527776
Замеры показывают, что добавление условия не привело к оптимизации.
Ускорение может быть только в единственном случае, когда на вход алгоритму дается уже отсортированный список.
'''