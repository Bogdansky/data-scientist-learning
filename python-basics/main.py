# Напиши функцию convert_and_sum(a, b), которая:
# принимает два аргумента (str),
# преобразует их в int,
# возвращает сумму.

def convert_and_sum(a, b):
    return int(a) + int(b)

# Напиши функцию max_of_three(a, b, c), которая возвращает наибольшее из трёх чисел.
def max_of_three(a,b,c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c

# Напиши функцию filter_even(nums), которая принимает список чисел и возвращает только чётные.
def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

# Напиши функцию count_letters(text), которая возвращает словарь с количеством 
# вхождений каждой буквы в строку. 
# Игнорируй пробелы и делай все буквы строчными.
def count_letters(text):
    dict = {}
    for char in text:
        dict[char] = dict.get(char, 0) + 1
    return dict

# Напиши функцию greet(name, is_morning), которая:
# возвращает "Доброе утро, {name}!" если is_morning == True,
# иначе — "Добрый вечер, {name}!".
def greet(name, is_morning):
    morning_template = "Доброе утро, {name}!"
    evening_template = "Добрый вечер, {name}!"
    template_touse = morning_template if is_morning else evening_template
    return template_touse.format(name=name)

print('convert_and_sum: ')
print(convert_and_sum("10", "20"))
print('max_of_three: ')
print(max_of_three(1, 7, 6))
print('filter_even: ')
print(filter_even([1, 2, 3, 4, 5, 6]))
print('count_letters: ')
print(count_letters("ahahahlol"))
print('greet: ')
print(greet("Богдан", True))   # → Доброе утро, Богдан!
print(greet("Ксения", False))  # → Добрый вечер, Ксения!