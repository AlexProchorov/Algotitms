import time


def measure_function(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        delta = end_time - start_time
        print("Took: ", delta, " seconds")
        return res
    return wrapper


@measure_function
def fill_list(number_of_items):
    test_list = []
    for iterator in range(number_of_items):
        test_list.append(iterator)
    return test_list


@measure_function
def fill_dict(number_of_items):
    test_dict = {}
    for iterator in range(number_of_items):
        test_dict[iterator] = iterator
    return test_dict


@measure_function
def get_item_from_list(list_to_process, item_to_find):
    return list_to_process[item_to_find]


@measure_function
def get_item_from_list_loop(list_to_process, item_to_find):
    for n in list_to_process:
        if n == item_to_find:
            return n


@measure_function
def get_item_from_dict(dict_to_process, item_to_find):
    return dict_to_process[item_to_find]


@measure_function
def get_item_by_value_list(list_to_process, number_to_find):
    for n in list_to_process:
        if n == number_to_find:
            return n


@measure_function
def get_item_by_value_dict(dict_to_process, number_to_find):
    for n in dict_to_process.values():
        if n == number_to_find:
            return n


print("Generating List...")
generated_list = fill_list(60000000)  # 3.3000006675720215
print("Generating Dict...")
generated_dict = fill_dict(60000000)  # 3.8124682903289795

"""
Добавление новых элементов в словарь происходит медленнее. При добавлении в словарь
интерперетатор должен считать хеши ключей.
"""

print("Get item from list by index...")
result = get_item_from_list(generated_list, 50000000)  # 0.0
print("Get item from list by index with loop...")
result = get_item_from_list_loop(generated_list, 50000000)  # 1.0189380645751953
print("Get item from dict by key...")
result = get_item_from_dict(generated_dict, 50000000)  # 0.0



print("Getting item with certain value from list...")
result = get_item_by_value_list(generated_list, 50000000)  # 0.9858968257904053
print("Getting item with certain value from dict...")
result = get_item_by_value_dict(generated_dict, 50000000)  # 1.249124526977539

"""
Извлечение элементов по их значениям из листа происходят быстрее, чем из словаря 
"""