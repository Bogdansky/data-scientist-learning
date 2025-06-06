import pandas as pd

# Задание 1
# Создай DataFrame:
# Имя: ["Аня", "Богдан", "Ксюша"]
# Город: ["Минск", "Брест", "Минск"]
# Возраст: [22, 30, 27]
# Сохрани его в файл people.csv без индекса.
df = pd.DataFrame({
    "Имя": ["Аня", "Богдан", "Ксюша"],
    "Город": ["Минск", "Брест", "Минск"],
    "Возраст": [22, 30, 27]
})
df.to_csv('./files/people.csv', index=False, encoding='utf-8')

# Задание 2
# Загрузи people.csv обратно в переменную df_loaded, выведи её и проверь, совпадает ли с исходной.
df_loaded = pd.read_csv('./files/people.csv', encoding='utf-8')
print(df_loaded)

# Задание 3
# Сохрани эту таблицу в формате JSON и Excel:
# people.json
# people.xlsx
df_loaded.to_json('./files/people.json', index=False, force_ascii=False)
df_loaded.to_excel('./files/people.xlsx', index=False)