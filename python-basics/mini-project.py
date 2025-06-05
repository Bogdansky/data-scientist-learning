import os
import matplotlib.pyplot as plt

def get_initial_text():
    script_dir = os.path.dirname(__file__)  # директория, где лежит этот скрипт
    path = os.path.join(script_dir, 'mini-project-1-input.txt')

    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            initial_text = f.read()
    else:
        initial_text = input("Введите текст для анализа: ")
    return initial_text

def clean_text(text): #→ str
    return "".join([char.lower() for char in text if char != ' '])

def count_letters(text): #→ dict
    result = {}
    for char in text:
        result[char] = result.get(char, 0) + 1
    return result

# Возвращает топ N букв по частоте
def top_letters(freq_dict, n): #→ list[tuple]
    sorted_items = sorted(freq_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:n]

# Сохраняет отчёт в файл
def save_report(filename, stats): #→ None
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(stats)

# Добавим функцию plot_top_letters, которая:
# принимает список топ-букв (буква, частота),
# рисует столбчатую диаграмму (bar chart),
# сохраняет её в файл top_letters.png
def plot_top_letters(top_items):
    letters = [item[0] for item in top_items]
    counts = [item[1] for item in top_items]

    plt.figure(figsize=(8, 5))
    plt.bar(letters, counts)
    plt.title("Топ букв по частоте")
    plt.xlabel("Буквы")
    plt.ylabel("Частота")
    plt.grid(axis='y')

    plt.savefig("top_letters.png", dpi=150)
    plt.close()

# Ввод текста (можно из input() или из файла)
# Вызов всех функций
# Печать отчёта и сохранение
def main():
    initial_text = get_initial_text()
    
    text = clean_text(initial_text)
    frequency_dict = count_letters(text)
    unique_chars_number = sum(1 for item in frequency_dict.items() if item[1] == 1)
    top_n_letters = top_letters(frequency_dict, 15)

    report = f'Введите текст: {initial_text}'
    report += f'\nКоличество символов (без пробелов): {len(text)}'
    report += f'\nУникальных букв: {unique_chars_number}'
    report += f'\nТоп 15 букв: '+ ''.join(f'\n{i[0]}: {i[1]}' for i in top_n_letters)

    save_report('stats.txt', report)
    plot_top_letters(top_n_letters)

if __name__ == "__main__":
    main()