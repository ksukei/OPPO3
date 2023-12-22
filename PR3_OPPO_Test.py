def check_document(file):
    with open(file, 'r') as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        line = line.strip()

        parts = line.split(' ')

        # Проверяем количество частей в строке
        if len(parts) < 3:
            print(f"Ошибка в отсутствии данных: строка {i + 1}")
            continue

        date = parts[0]
        product = parts[1]
        amount = parts[2]

        # Проверяем количество частей в строке
        if len(parts) < 3:
            print(f"Ошибка в отсутствии данных: строка {i + 1}")
            continue

        try:
            year, month, day = parts[0].split('.')
            int(year)
            int(month)
            int(day)
        except ValueError:
            print(f"Ошибка в формате записи даты: строка {i + 1}")
            continue

        year = int(year)
        month = int(month)
        day = int(day)

        if month == 2 and day > 28 and year % 4 != 0:
            print(f"Ошибка в феврале в невисокосный год: строка {i + 1}")
            continue

        # Проверяем количество дней в месяце
        if month in [1, 3, 5, 7, 8, 10, 12] and day > 31:
            print(f"Нет 32 дня в январе, марте, мае, июле, августе, октябре, декабре: строка {i + 1}")
            continue

        if month in [4, 6, 9, 11] and day > 30:
            print(f"Нет 31 дня в апреле, июне, сентябре, ноябре: строка {i + 1}")
            continue

        if len(parts[0]) != 10:
            print(f"Ошибка ввода данных (общая): строка {i + 1}")
            continue

        if year == 0:
            print(f"Ошибка нулевого года: строка {i + 1}")
            continue

        if not product.isalpha() or not all(ord(char) < 128 for char in product):
            print(f"Ошибка в названии продукта (кириллица): строка {i + 1}")
            continue

        if not amount.isdigit():  # Проверка цены на целое число
            print(
                f"Ошибка в цене (целое число или неопознанные символы, как + - = / \ : * ? < > | _ ( ) ): строка {i + 1}")
            continue

    print("Проверка завершена")


check_document("in.txt")
