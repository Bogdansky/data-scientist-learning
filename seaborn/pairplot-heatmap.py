import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Примерные данные
data = {
    "Имя": ["Аня", "Богдан", "Илья", "Катя", "Олег", "Нина"],
    "Возраст": [21, 23, 19, 22, 24, 20],
    "Баллы": [85, 92, 78, 88, 95, 83],
    "Курс": [2, 3, 1, 2, 3, 1]
}

df = pd.DataFrame(data)

# 1. 
# Построить pairplot
# Для всех числовых признаков (Возраст, Баллы, Курс)
# Используй цветовую группировку по Курс
sns.pairplot(data=df, hue='Курс')
plt.show()

# 2. Построить heatmap
# Для корреляционной матрицы числовых признаков
# Используй цветовую палитру "coolwarm"
# Включи аннотации значений (annot=True)
corr = df[['Баллы', 'Курс', 'Возраст']].corr()
sns.heatmap(corr, cmap='coolwarm', annot=True, vmin=-1, vmax=1)
plt.show()