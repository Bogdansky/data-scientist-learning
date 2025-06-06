import pandas as pd

# Задание 1
# Создай DataFrame с пропущенными значениями:
df = pd.DataFrame({
    "Имя": ["Анна", "Богдан", None, "Катя"],
    "Возраст": [22, 30, 19, None],
    "Город": ["Минск", None, "Минск", "Гомель"]
})

# Задание 2
# Сделай следующее:
# Найди, в каких строках есть хотя бы одно NaN
# Удали строки с пропущенным "Городом"
# Заполни пропущенные значения в "Имя" значением "Неизвестно"
# Заполни пропущенные значения в "Возраст" средним возрастом по остальным
lines_with_nan = df[df.isna().any(axis=1)]
print(lines_with_nan)
without_na_city = df.dropna(subset="Город")
print(without_na_city)
df["Имя"] = df["Имя"].fillna("Неизвестно")
print(df)
average_age = df["Возраст"].mean().round(0)
print(average_age)
df["Возраст"] = df["Возраст"].fillna(average_age)
print(df)