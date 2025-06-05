import numpy as np

# ✅ Задание 1
# Создай массив из чисел от 0 до 9 включительно.
def create_digit_array():
    return np.arange(0, 10, 1)

# ✅ Задание 2
# Создай массив 3×4, заполненный единицами.
def create_two_dimensional_array():
    return np.ones((3,4))

# ✅ Задание 3
# Создай массив 5 случайных целых чисел от 1 до 100.
def create_5_random_digits_array():
    return np.random.randint(1, 100, size=5)

# ✅ Задание 4
# Создай массив a = [1, 2, 3] и выведи a + a, a * 3, a ** 2.
def manipulate_with_array():
    a = np.array([1, 2, 3])
    print(a + a)
    print(a * 3)
    print(a ** 2)

# ✅ Задание 5
# Создай двумерный массив 3×3, и посчитай:
# сумму всех элементов
# среднее значение
# транспонированную матрицу
def do_matrix_things():
    matrix = np.array([
        np.random.randint(1, 20, size=3),
        np.random.randint(1, 20, size=3),
        np.random.randint(1, 20, size=3)
    ])
    print(matrix)
    # сумма всех элементов
    print(np.sum(matrix))
    # среднее значение
    print(np.average(matrix))
    # транспонированная матрица
    print(np.transpose(matrix))

print('Задание 1')
print(create_digit_array())

print('Задание 2')
print(create_two_dimensional_array())

print('Задание 3')
print(create_5_random_digits_array())

print('Задание 4')
manipulate_with_array()

print('Задание 5')
do_matrix_things()