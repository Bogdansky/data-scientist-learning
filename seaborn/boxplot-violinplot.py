import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Имя": ["Аня", "Богдан", "Илья", "Катя", "Олег", "Нина"],
    "Возраст": [21, 23, 19, 22, 24, 20],
    "Баллы": [85, 92, 78, 88, 95, 83],
    "Курс": [2, 3, 1, 2, 3, 1]
})

#region Examples
## Boxplot — сравнение баллов по курсу
# plt.figure(figsize=(6, 4))
# sns.boxplot(data=df, x="Курс", y="Баллы")
# plt.title("Boxplot: Баллы по курсам")
# plt.grid(True)
# plt.show()

## Violinplot — с формой распределения
# plt.figure(figsize=(6, 4))
# sns.violinplot(data=df, x="Курс", y="Баллы", inner="quartile")  # quartile — покажет медиану и квартили
# plt.title("Violinplot: Баллы по курсам")
# plt.grid(True)
# plt.show()
#endregion

# Задание: Анализ успеваемости по курсам
# 📌 Шаг 1 — Создай DataFrame 
df = pd.DataFrame({
    "Курс": [2]*7,
    "Баллы": [70, 72, 74, 76, 78, 80, 150]  # 👈 150 — ЯВНЫЙ выброс
})

# 📌 Шаг 2 — Построй 2 графика
# Boxplot, где:
# по оси X: Курс
# по оси Y: Баллы
# цель: увидеть медиану и разброс
# &
# Violinplot с теми же параметрами, но:
# добавь аргумент inner="quartile" для отображения медианы и квартилей внутри
plt.figure(figsize=(5,6))
sns.boxplot(df, x='Курс', y='Баллы')
plt.title='Разброс баллов по курсам'
plt.grid(True)
plt.show()

plt.figure(figsize=(5,6))
sns.violinplot(data=df, x='Курс', y='Баллы', inner='quartile')
plt.title='Форма распределения баллов по курсам'
plt.grid(True)
plt.show()