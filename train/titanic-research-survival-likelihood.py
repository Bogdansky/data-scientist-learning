import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: read the data
df = pd.read_csv('train_titanic.csv', encoding='utf-8')

# Step 2: draw hystogram of survival by sex 
# (let's assume that sex=0 means male and sex=1 means females)
sns.countplot(data=df, x="Sex", hue="Survived")
plt.title("Выживаемость по полу")
plt.show()

# Step 3: draw hystogram of survival by class
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title('Выживаемость по классу')
plt.show()

# Step 4: draw boxplot of survival by age
sns.boxplot(data=df, x='Survived', y='Age')
plt.title("Возраст по группам выживаемости")
plt.show()

# Step 5: draw hystogram of age by "survived" and "not survived"
sns.histplot(data=df[df["Survived"] == 0], x="Age", bins=20, color="red", label="Не выжил", kde=True)
sns.histplot(data=df[df["Survived"] == 1], x="Age", bins=20, color="green", label="Выжил", kde=True)
plt.legend()
plt.title("Возраст и выживаемость")
plt.show()

# Step 6 (my wish): draw hystogram of sex by "survived" and "not survived"
sns.countplot(data=df, x="Sex", hue="Survived")
plt.legend()
plt.xlabel='Пол'
plt.title("Возраст и выживаемость")
plt.show()

# Step Correlation
corr = df[['Sex', 'Age', 'Pclass', 'Survived']].corr()

sns.heatmap(corr, vmin=-1, vmax=1, cmap='coolwarm', annot=False)
plt.show()