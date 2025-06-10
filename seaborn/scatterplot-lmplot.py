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

# ✅ Диаграмма рассеяния
plt.figure()
sns.scatterplot(data=df, x="Возраст", y="Баллы")
plt.title("Диаграмма рассеяния: возраст vs баллы")
plt.xlabel("Возраст")
plt.ylabel("Баллы")
plt.grid(True)
plt.show()

# ✅ Линия регрессии
lm = sns.lmplot(data=df, x="Возраст", y="Баллы")
lm.figure.suptitle("Регрессионная зависимость: возраст и баллы", y=1.03)
plt.grid(True)
plt.show()