# goit-algo-hw-03
Homework for the topic “Recursive functions, algorithms and examples of their application”

task_1
Парсинг аргументів:

Код використовує argparse для обробки шляхів до вихідної та цільової директорій.
Якщо цільову директорію не вказано, вона за замовчуванням встановлюється в dist.
Рекурсивне читання директорій:

Функція process_directory перевіряє кожен елемент у вказаній директорії.
Якщо елемент - директорія, функція викликає саму себе.
Якщо елемент - файл, він передається на обробку в process_file.
Копіювання файлів:

Визначається розширення файлу і створюється відповідна піддиректорія.
Файл копіюється в цю піддиректорію.
Обробка помилок:

Помилки доступу до файлів або директорій обробляються з виведенням повідомлень.
Результат:

Файли з вихідної директорії копіюються в цільову і сортуються за розширеннями.

Translated with DeepL.com (free version)

task 2
Функція move_disks:

Ця функція реалізує основну логіку розв'язання задачі Ханойських башт.
Якщо кількість дисків n == 1, найменший диск переміщується зі стрижня source на target.
Для більшої кількості дисків (n > 1):
Спершу переміщуємо n-1 дисків на допоміжний стрижень (auxiliary).
Потім переміщуємо найбільший диск на кінцевий стрижень (target).
Нарешті, переміщуємо n-1 дисків із допоміжного стрижня на кінцевий.
Функція main:

Програма запитує в користувача кількість дисків.
Ініціалізує початковий стан стрижнів.
Викликає функцію move_disks для розв'язання задачі.
Після завершення відображає кінцевий стан стрижнів.
Логування стану:

Після кожного переміщення програма виводить поточний стан стрижнів, щоб користувач міг зрозуміти, що відбувається на кожному кроці.
