# Бесконечный цикл для перезапуска всей игры целиком
while True:
    print("\n--- ДОБРО ПОЖАЛОВАТЬ В ВИКТОРИНУ 'ГОД РОЖДЕНИЯ' ---")

    celebrities = [
        {"name": "А.С. Пушкин", "year": 1799},
        {"name": "П.И. Чайковский", "year": 1840},
        {"name": "Юрий Гагарин", "year": 1934},
        {"name": "Альберт Эйнштейн", "year": 1879},
        {"name": "Леонардо да Винчи", "year": 1452},
    ]

    # Переменные для подсчета результатов
    correct_answers = 0
    wrong_answers = 0
    total_questions = len(celebrities)

    for person in celebrities:
        while True:
            user_input = input(f"В каком году родился {person['name']}? ")

            # Проверяем, что введены именно цифры
            if user_input.isdigit():
                user_year = int(user_input)
                break  # Ввод корректный, выходим из цикла проверки
            else:
                print("Пожалуйста, введите год числами!")

        # Проверяем правильность ответа
        if user_year == person["year"]:
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"Неверно! (Правильный ответ: {person['year']})")
            wrong_answers += 1

    # Считаем проценты по формуле из задания
    percent_correct = correct_answers * 100 / total_questions
    percent_wrong = wrong_answers * 100 / total_questions

    # Выводим статистику на экран
    print("\n====== ИТОГИ ВИКТОРИНЫ ======")
    print(f"Количество правильных ответов: {correct_answers}")
    print(f"Количество ошибок: {wrong_answers}")
    print(f"Процент правильных ответов: {percent_correct}%")
    print(f"Процент неправильных ответов: {percent_wrong}%")
    print("=============================")

    # --- НОВЫЙ БЛОК ПРОВЕРКИ ДЛЯ ВЫХОДА ИЗ ИГРЫ ---
    while True:
        play_again = input("\nХотите начать игру сначала? (да/нет): ").lower().strip()

        if play_again == "да" or play_again == "нет":
            break  # Пользователь ввёл корректное слово, выходим из проверки ввода
        else:
            print("Пожалуйста, введите чётко слово 'да' или 'нет'!")

    if play_again == "нет":
        print("Спасибо за игру! До свидания!")
        break  # Выходим из главного цикла, программа завершается
