bank = {245: "340 рублей", 278: "5000 рублей", 900: "3 рубля"}
number_yacheika = int(input("Ваш номер ячейки"))
try:
    money = bank[number_yacheika]
    print(f"У вас {money} рублей на счету")
except:
    print("Такой ячейки нет")