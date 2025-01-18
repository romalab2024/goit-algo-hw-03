def move_disks(n, source, target, auxiliary, state):
    """
    Рекурсивна функція для розв'язання задачі Ханойських башт.

    :param n: Кількість дисків.
    :param source: Початковий стрижень (A).
    :param target: Кінцевий стрижень (C).
    :param auxiliary: Допоміжний стрижень (B).
    :param state: Словник зі станом стрижнів.
    """
    if n == 1:
        # Переміщуємо найменший диск з source на target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
    else:
        # Переміщуємо n-1 дисків з source на auxiliary
        move_disks(n - 1, source, auxiliary, target, state)

        # Переміщуємо найбільший диск з source на target
        move_disks(1, source, target, auxiliary, state)

        # Переміщуємо n-1 дисків з auxiliary на target
        move_disks(n - 1, auxiliary, target, source, state)

def main():
    """
    Основна функція для виконання програми.
    """
    try:
        n = int(input("Введіть кількість дисків: "))
        if n <= 0:
            print("Кількість дисків має бути додатнім числом.")
            return

        # Початковий стан стрижнів
        state = {
            'A': list(range(n, 0, -1)),  # Диски розміщені за зменшенням розміру
            'B': [],
            'C': []
        }

        print(f"Початковий стан: {state}")
        move_disks(n, 'A', 'C', 'B', state)
        print(f"Кінцевий стан: {state}")

    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
