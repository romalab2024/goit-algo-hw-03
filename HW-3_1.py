import os
import shutil
import argparse

def parse_arguments():
    """
    Функція для розбору аргументів командного рядка.
    Скрипт приймає два аргументи:
    1. Шлях до вихідної директорії.
    2. Шлях до директорії призначення (за замовчуванням 'dist').
    """
    parser = argparse.ArgumentParser(description="Рекурсивне копіювання і сортування файлів за розширеннями.")
    parser.add_argument("source", type=str, help="Шлях до вихідної директорії.")
    parser.add_argument("destination", type=str, nargs="?", default="dist", help="Шлях до директорії призначення. За замовчуванням 'dist'.")
    return parser.parse_args()

def process_directory(source_dir, dest_dir):
    """
    Рекурсивне читання вмісту директорії та обробка кожного елемента.

    :param source_dir: Шлях до вихідної директорії.
    :param dest_dir: Шлях до директорії призначення.
    """
    try:
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)  # Повний шлях до елемента

            if os.path.isdir(source_item):
                # Якщо елемент - директорія, обробляємо її рекурсивно
                process_directory(source_item, dest_dir)
            elif os.path.isfile(source_item):
                # Якщо елемент - файл, обробляємо його для копіювання
                process_file(source_item, dest_dir)
    except Exception as e:
        print(f"Помилка під час обробки директорії {source_dir}: {e}")

def process_file(source_file, dest_dir):
    """
    Копіює файл у піддиректорію на основі його розширення.

    :param source_file: Шлях до вихідного файлу.
    :param dest_dir: Шлях до директорії призначення.
    """
    try:
        # Отримання розширення файлу (без крапки)
        file_extension = os.path.splitext(source_file)[1][1:].lower() or "no_extension"
        target_subdir = os.path.join(dest_dir, file_extension)  # Директорія для даного типу файлів

        # Створюємо піддиректорію, якщо її ще немає
        os.makedirs(target_subdir, exist_ok=True)

        # Копіюємо файл у піддиректорію
        shutil.copy2(source_file, target_subdir)
        print(f"Скопійовано файл: {source_file} -> {target_subdir}")
    except Exception as e:
        print(f"Помилка під час обробки файлу {source_file}: {e}")

def main():
    """
    Основна функція програми. Виконує наступні дії:
    1. Розбирає аргументи командного рядка.
    2. Перевіряє існування вихідної директорії.
    3. Створює директорію призначення.
    4. Рекурсивно обробляє вміст вихідної директорії.
    """
    args = parse_arguments()

    source_dir = args.source
    dest_dir = args.destination

    if not os.path.exists(source_dir):
        print(f"Вихідна директорія {source_dir} не існує.")
        return

    # Створюємо директорію призначення, якщо вона не існує
    os.makedirs(dest_dir, exist_ok=True)

    # Рекурсивно обробляємо вихідну директорію
    process_directory(source_dir, dest_dir)

    print(f"Файли успішно скопійовано та відсортовано у директорію {dest_dir}.")

if __name__ == "__main__":
    main()
