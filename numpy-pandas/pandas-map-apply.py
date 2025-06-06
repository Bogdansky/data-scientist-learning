import pandas as pd

# Задание 1
# Создай DataFrame:
# Имя: ["Аня", "Богдан", "Катя"]
# Город: ["Минск", "Брест", "Минск"]
def get_data_frame():
    return pd.DataFrame({
        "Имя": ["Аня", "Богдан", "Катя"],
        "Город": ["Минск", "Брест", "Минск"]
    })

# Задание 2
# Создай столбец "Приветствие", в котором будет:
# "Привет, <Имя> из <Город>!"
# (используй apply по строкам)
def add_greetings_column(data_frame):
    data_frame["Приветствие"] = data_frame.apply(lambda row: f'Привет, {row["Имя"]} из {row["Город"]}!', axis=1)

# Задание 3
# Преобразуй имена в верхний регистр через map или apply
def make_names_uppper_case(data_frame):
    data_frame["Имя"] = data_frame["Имя"].map(str.upper)

print("Задание 1")
df = get_data_frame()
print(df)

print("Задание 2")
add_greetings_column(df)
print(df)

print("Задание 3")
make_names_uppper_case(df)
print(df)