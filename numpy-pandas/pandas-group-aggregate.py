import pandas as pd

# Задание 1
# Создай DataFrame:
# Имя      Город     Возраст
# Анна     Минск     22  
# Богдан   Брест     30  
# Илья     Минск     19  
# Катя     Минск     25  
# Олег     Брест     28
def get_data_frame():
    return pd.DataFrame({
        "Имя": [
            "Анна",
            "Богдан",
            "Илья",
            "Катя",
            "Олег",
        ],
        "Город": ["Минск","Брест","Минск","Минск","Брест"],
        "Возраст": [22,30,19,25,28]
    })

# Задание 2
# Посчитай средний возраст по городам
# Посчитай, сколько людей в каждом городе
# Выведи максимальный возраст по каждому городу
def get_stats(data_frame):
    stats = {}
    grouped_by_city = data_frame.groupby("Город")
    stats["city_average_age"] = grouped_by_city["Возраст"].mean().astype(int)
    stats["people_number"] = grouped_by_city["Имя"].count()
    stats["city_max_age"] = grouped_by_city["Возраст"].max()

    return stats

print('Задание 1')
data_frame = get_data_frame()
print(data_frame)

print('Задание 2')
stats = get_stats(data_frame)
print('Средний возраст по городам:' + ''.join(f'\n{avg[0]}: {avg[1]}' for avg in stats['city_average_age'].items()))
print('Число людей по городам:' + ''.join(f'\n{people[0]}: {people[1]}' for people in stats['people_number'].items()))
print('Максимальный возраст по городам:' + ''.join(f'\n{max_age[0]}: {max_age[1]}' for max_age in stats['city_max_age'].items()))