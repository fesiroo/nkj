def experiment(reag1, reag2):
    if reag1 == "Варенье":
        if reag2 == "Вода":
            colour = "красный"
        elif reag2 == "Яблочный сок":
            colour = "темно-красный"
        else:
            print("Такого реагента нет")
    elif reag1 == "Вода":
        if reag2 == "Яблочный сок":
            colour = "оранжевый"
        elif reag2 == "Варенье":
            colour = "красный"
        else:
            print("Такого реагента нет")
    elif reag1 == "Яблочный сок":
        if reag2 == "Варенье":
            colour = "темно-красный"
        elif reag2 == "Вода":
            colour = "оранжевый"
        else:
            print("Такого реагента нет")
    print(f"Получился {colour} цвет")
reag1 = input("Введите первый реагент")
reag2 = input("Введите второй реагент")
experiment(reag1, reag2)


    