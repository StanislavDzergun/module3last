def calculate_structure_sum(data_structure):
    sum = 0
    if isinstance(data_structure, int):              # проверяем содержаться ли в data_structure целые числа
        sum += data_structure                        # если содержаться, то сумм все числа
    if isinstance(data_structure, str):              # проверяем содержаться ли в data_structure типы строки
        sum += len(data_structure)                   # если содержаться, то сумм кол-во длин всех строк строки
    if isinstance(data_structure, list):             # проверяем содержаться ли в data_structure типы списка
        for i in data_structure:
            sum += calculate_structure_sum(i)        # если содержаться, то сумм кол-во длин всех строк списка
    if isinstance(data_structure, tuple):            # проверяем содержатся ли в data_structure типы кортежей
        for i in data_structure:
            sum += calculate_structure_sum(i)        # если содержаться, то сумм кол-во длин всех строк кортежа
    if isinstance(data_structure, set):              # проверяем наличие множеств в data_structure
        for i in data_structure:
            sum += calculate_structure_sum(i)        # если содержаться,то сумм кол-во длин всех строк множества
    if isinstance(data_structure, dict):             # проверяем наличие словарей в data_structure
        for key, value in data_structure.items():
            sum += calculate_structure_sum(key)      #при содерж сумм кол-во всех строк ключей
            sum += calculate_structure_sum(value)    #при содерж сумм знач всех строк значений
    return sum                                       #возвр сумму


data_structure = [                                   #исход данные
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)     #вывод рез
print(result)