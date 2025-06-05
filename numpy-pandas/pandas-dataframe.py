import pandas as pd

# Задание 1
# Создай DataFrame из следующих данных:
# {"Имя": ["Анна", "Богдан", "Илья"], "Возраст": [22, 30, 19], "Город": ["Минск", "Брест", "Гомель"]}
def create_data_frame():
    return pd.DataFrame({
        "Имя": ["Анна", "Богдан", "Илья"], 
        "Возраст": [22, 30, 19], 
        "Город": ["Минск", "Брест", "Гомель"]
    })

# Задание 2
# Выведи:
# только столбец "Имя"
# всех, кто старше 20 лет
def get_names_older_20(data_frame):
    return list(data_frame[data_frame["Возраст"] > 20]["Имя"])

# Задание 3
# Добавь новый столбец "Возраст + 5", где возраст увеличен на 5 лет
def add_new_column(data_frame):
    data_frame["Возраст + 5"] = data_frame["Возраст"] + 5

print("Задание 1")
data_frame = create_data_frame()
print(data_frame)

print("Задание 2")
print(get_names_older_20(data_frame))

print("Задание 3")
add_new_column(data_frame)
print(data_frame)