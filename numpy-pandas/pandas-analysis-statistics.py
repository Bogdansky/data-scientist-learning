import pandas as pd
import matplotlib.pyplot as plt

# Задание 1 — создаём таблицу студентов
# Имя:     ["Аня", "Богдан", "Илья", "Катя", "Олег", "Нина"]
# Возраст: [21, 23, 19, 22, 24, 20]
# Баллы:   [85, 92, 78, 88, 95, 83]
# Курс:    [2, 3, 1, 2, 3, 1]
def get_data_frame():
    return pd.DataFrame({
        "Имя": ["Аня", "Богдан", "Илья", "Катя", "Олег", "Нина"],
        "Возраст": [21, 23, 19, 22, 24, 20],
        "Баллы": [85, 92, 78, 88, 95, 83],
        "Курс": [2, 3, 1, 2, 3, 1]
    })

# Задание 2 — рассчитай:
# средний и медианный балл
# стандартное отклонение и дисперсию баллов
# минимальный и максимальный возраст
def calculate_atomic_statistic_values(data_frame):
    return {
        "average": data_frame["Баллы"].mean(),
        "median": data_frame["Баллы"].median(),
        "average_deviation": data_frame["Баллы"].std(),
        "dispersion": data_frame["Баллы"].var(),
        "min_age": data_frame["Возраст"].min(),
        "max_age": data_frame["Возраст"].max(),
    }

# Задание 3 — вычисли корреляцию между:
# Возрастом и Баллами
def calculate_age_mark_correlation(data_frame):
    return data_frame[["Возраст", "Баллы"]].corr()

# Задание 4 (по желанию) — визуализация:
# гистограмма (hist())
# диаграмма рассеяния (scatter)
def draw_hist_scatter(data_frame):
    draw_hist(data_frame)
    draw_scatter(data_frame)

def draw_hist(data_frame):
    values = data_frame["Баллы"]

    plt.hist(values, bins=5, edgecolor='black')
    plt.title("Распределение значений")
    plt.xlabel("Значения")
    plt.ylabel("Частота")
    plt.show()

def draw_scatter(data_frame):
    subset = data_frame[["Возраст", "Баллы"]]
    print(subset)
    subset.plot.scatter(x="Возраст", y="Баллы")

    plt.title("Зависимость баллов от возраста")
    plt.xlabel("Возраст")
    plt.ylabel("Баллы")
    plt.grid(True)
    plt.show()

print('Задание 1')
df = get_data_frame()
print(df)

print('Задание 2')
stats = calculate_atomic_statistic_values(df)
print(f'Средний бал: {stats["average"].round(2)}')
print(f'Медианный бал: {stats["median"].round(2)}')
print(f'Стандартное отклонение баллов: {stats["average_deviation"].round(2)}')
print(f'Дисперсия баллов: {stats["dispersion"].round(2)}')
print(f'Минимальный возраст: {stats["min_age"]}')
print(f'Максимальный возраст: {stats["max_age"]}')

print('Задание 3')
age_mark_correlation = calculate_age_mark_correlation(df)
print(f'Корреляция возраста и баллов:\n{age_mark_correlation}')

print('Задание 4')
draw_hist_scatter(df)