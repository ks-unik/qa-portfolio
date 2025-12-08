while True:
    try:
        # Ввод числа людей на кофе-брейке
        num_people = int(input("Enter the number of people at the coffee break:\n"))

        # Проверка корректности диапазона
        if 1 <= num_people <= 2*10**9:
            # Изначально у нас 1 кусок рулета
            pieces = 1
            # Счётчик разрезов
            cuts = 0

            # Цикл продолжается, пока количество кусков меньше числа людей
            while pieces < num_people:  
                # Удваиваем количество кусков (делаем разрезы через "бесконечное лезвие")
                pieces *= 2
                # Увеличиваем счётчик разрезов
                cuts += 1

                # Если после удвоения мы превысили нужное количество кусков,
                # нужно "откатить" лишние куски
                if pieces > num_people:
                    excess = pieces - num_people  # вычисляем лишние куски
                    pieces -= excess              # корректируем количество кусков

            # Выводим минимальное количество разрезов
            print(cuts)
            break  # выходим из основного цикла после корректного ввода
        else:
            # Сообщение, если число вне диапазона
            print("Enter a number between 1 and 2·10⁹, inclusive.")
            continue

    except ValueError:
        # Сообщение при вводе некорректных данных (не целого числа)
        print("Invalid input. Please enter an integer number.")
