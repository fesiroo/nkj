a = 10
# if a1 > 5:
#     print("true")

# print(a+b)

# a = int("hi")

# print(1+"2")

# try:
#     a = int(input("Введите число"))
# except:
#     print("это не число")

# try:
#     a = int(input("введите 1 число "))
#     b = int(input("введите 2 число "))
#     c = a/b
#     print(c)
# except ValueError:
#     print("нельзя вводить строку")
# except ZeroDivisionError:
#     print("нельзя делить на 0")

# try:
#     a = input("введите число")
#     a = int(a)
# except ValueError:
#     print("ошибка")
# else:
#     print(f"вы ввели число {a}")
# finally:
#     print("конец программы")

while True:
    a = input("Введите число: ")
    b = input("Введите второе число: ")
    try:
        result = int(a)/int(b)
    except ValueError:
        print("это не число")
    except ZeroDivisionError:
        print("на ноль делить нельзя")
    else:
        print(result)
        break
