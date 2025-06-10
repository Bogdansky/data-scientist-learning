import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Данные
df = pd.DataFrame({
    "Имя": ["Аня", "Богдан", "Илья", "Катя", "Олег", "Нина"],
    "Возраст": [21, 23, 19, 22, 24, 20],
    "Баллы": [85, 92, 78, 88, 95, 83],
    "Курс": [2, 3, 1, 2, 3, 1]
})

sns.histplot(df["Баллы"], bins=5, edgecolor="black", color="skyblue")
plt.title("Гистограмма баллов студентов")
plt.xlabel("Баллы")
plt.ylabel("Частота")
plt.grid(True)
plt.show()

sns.kdeplot(df["Баллы"], fill=True, color="orange")
plt.title("Плотность распределения баллов")
plt.xlabel("Баллы")
plt.ylabel("Плотность")
plt.grid(True)
plt.show()

sns.histplot(df["Баллы"], bins=5, kde=True, edgecolor="black", color="lightgreen")
plt.title("Гистограмма + KDE баллов")
plt.xlabel("Баллы")
plt.ylabel("Частота / Плотность")
plt.grid(True)
plt.show()