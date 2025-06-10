import pandas as pd

df = pd.read_csv('train_titanic.csv', encoding='utf-8')
print(df)

# Шаг 1: выбираем имена колонок, в которых есть "zero"
zero_columns = [col for col in df.columns if 'zero' in col]
print(zero_columns)
# Шаг 2: фильтруем только те, в которых все значения равны нулю
zero_only_columns = [col for col in zero_columns if (df[col] == 0).all()]
print(zero_columns)

# Шаг 3: удаляем их
df = df.drop(columns=zero_only_columns)

df.to_csv('train_titanic.csv', encoding='utf-8', index=False)