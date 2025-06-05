import numpy as np

# Задание 1:
# Создай массив от 1 до 20. Получи только чётные элементы.
def get_even_items():
    arr = np.arange(1, 21)
    mask = arr % 2 == 0
    return arr[mask]

# Задание 2:
# Создай матрицу 3×4 со случайными числами. Выведи:
# вторую строку
# последний столбец
# подматрицу из центральных 4 элементов
def manipulate_with_matrix():
    random_matrix = np.random.randint(0, 10, size=(3,4))
    print(random_matrix)
    print(random_matrix[1])
    print(random_matrix[:, -1])
    print(random_matrix[1:, 1:-1])

# Задание 3:
# Создай массив из 10 случайных чисел от 1 до 100. Выведи только те, которые делятся на 3.
def get_3_division():
    rand_arr = np.random.randint(1, 100, size=10)
    print(rand_arr)
    mask = rand_arr % 3 == 0
    return rand_arr[mask]

print('Задание 1')
print(get_even_items())

print('Задание 2')
manipulate_with_matrix()

print('Задание 3')
print(get_3_division())