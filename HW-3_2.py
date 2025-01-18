import turtle

def draw_koch_segment(t, length, level):
    """
    Рекурсивна функція для малювання одного сегмента сніжинки Коха.

    :param t: Об'єкт turtle.
    :param length: Довжина сегмента.
    :param level: Рівень рекурсії.
    """
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)
        t.right(120)
        draw_koch_segment(t, length, level - 1)
        t.left(60)
        draw_koch_segment(t, length, level - 1)

def draw_koch_snowflake(length, level):
    """
    Функція для малювання повної сніжинки Коха.

    :param length: Довжина сторони сніжинки.
    :param level: Рівень рекурсії.
    """
    screen = turtle.Screen()
    screen.setup(width=800, height=800)
    screen.title("Сніжинка Коха")

    t = turtle.Turtle()
    t.speed("fastest")

    # Малюємо три сторони сніжинки
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

    screen.mainloop()

def main():
    """
    Основна функція для взаємодії з користувачем.
    """
    try:
        level = int(input("Введіть рівень рекурсії (наприклад, 3): "))
        if level < 0:
            print("Рівень рекурсії не може бути від'ємним.")
            return
        
        length = 300  # Початкова довжина сторони
        draw_koch_snowflake(length, level)
    except ValueError:
        print("Будь ласка, введіть ціле число.")

if __name__ == "__main__":
    main()
