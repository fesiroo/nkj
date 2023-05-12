import random
import time
class Player:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.level = 1
        self.exp = 0
        self.skill = None
    def create_player(name, race, job):
        hp = 0
        damage = 0
        if race == races[0]:
            hp += 2000
            damage += 1800
        elif race == races[1]:
            hp += 1500
            damage += 1200
        elif race == races[2]:
            hp += 900
            damage += 2000
        elif race == races[3]:
            hp += 2500
            damage += 1670
        else:
            print("Вы ошиблись")
        if job == jobs[0]:
            hp += 700
            damage += 3000
        elif job == jobs[1]:
            hp += 2000
            damage += 2000
        elif job == jobs[2]:
            hp += 2700
            damage += 3300
        elif job == jobs[3]:
            hp += 2790
            damage += 3400
        else:
            print("Вы ошиблись")
        return Player(name, hp, damage)
    def attack(self, victim):
        max_exp = self.level * 200
        victim.hp -= self.damage
        if victim.hp <= 0:
            print("Жертва умерла")
            print("Вы получили: 200 exp" )
            self.exp += 200
            if self.exp >= max_exp:
                self.level_up(max_exp)
            thing = random.randint(0,3)
            if thing == 1:
                wpn = self.create_weapon()
                print(f"Вам выпало оружие, {wpn[0]}, {wpn[1]}")
                time.sleep(1)
            elif thing == 2:
                df = self.create_defense()
                print(f"У вас теперь есть защита, {df[0]}, {df[1]}")
                time.sleep(1)
            elif thing == 3:
                fd = self.create_food()
                print(f"У вас теперь есть еда, {fd}")
                time.sleep(1)
            else:
                print("Вам ничего не выпало")
                time.sleep(1)
            self.skill = random.choice(powers)
            print(f"У вас есть супер сила, {self.skill}")
            time.sleep(2)
            return False
        else:
            if self.skill is not None:
                ability()
            print("Жертва жива", victim.hp, victim.damage)
            return True
    def level_up(self, max_exp):
        self.exp -= max_exp
        self.level += 1
        self.damage += self.level * 2
        self.hp += self.hp * 2
        print(f"Поздравляю с повышением уровня {self.level}")
        time.sleep(1)
    def create_weapon(self):
        weapon_type = weapon[random.randint(0, 4)]
        weapon_rare = random.choice(list(weapon_dict.keys()))
        if weapon_type == weapon[0]:
            self.damage += 140 * weapon.rare
        elif weapon_type == weapon[1]:
            self.damage += 170 * weapon_rare
        elif weapon_type == weapon[2]:
            self.damage += 150 * weapon_rare
        elif weapon_type == weapon[3]:
            self.damage += 160 * weapon_rare
        elif weapon_type == weapon[4]:
            self.damage += 200 * weapon_rare
        return weapon_type, weapon_dict[weapon_rare]
    def create_defense(self):
        defense_type = defense[random.randint(0, 4)]
        defense_rare = random.choice(list(defense_dict.keys()))
        if defense_type == defense[0]:
            self.hp += 300 * defense_rare
        elif defense_type == defense[1]:
            self.hp += 240 * defense_rare
        elif defense_type == defense[2]:
            self.hp += 250 * defense_rare
        elif defense_type == defense[3]:
            self.hp += 260 * defense_rare
        elif defense_type == defense[4]:
            self.hp += 270 * defense_rare
        return defense_type, defense_dict[defense_rare]
    def create_food(self):
        food =  random.choice(list(food_dict.keys()))
        self.hp += food 
        return food_dict[food]
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
    def enemy_create():
        rnd_name= random.choice(enemies)
        rnd_hp = random.randint(6000,8000)
        rnd_damage = random.randint(3900, 5000)
        return Enemy(rnd_name, rnd_hp, rnd_damage)
    def attack(self, victim):
        victim.hp -= self.damage
        if victim.hp <= 0:
            print("Вы проиграли")
            time.sleep(1)
            quit()
        else:
            print("Вы живы")
            time.sleep(1)
def choice():
    ask = input("Хотите ли вы разиться?")
    if ask == "Да":
        result = hero.attack(enemy)
        if result == True:
            enemy.attack(hero)
            choice()
    elif ask == "Нет":
        print("Вы решили пройти мимо")
    else:
        print("Напишите еще раз")
        choice()
def ability():
    if hero.skill == "замораживание":
        print("вы заморозили врага")
        enemy.damage = 0
        time.sleep(1)
    elif hero.skill == "поджигание":
        print("вы подожгли врага")
        enemy.hp = 0
        time.sleep(1)
    elif hero.skill == "отравление":
        print("вы отравили врага")
        enemy.hp -= 500
        time.sleep(1)
    elif hero.skill == "лечение":
        print("вы подлечились")
        hero.hp += 700
        time.sleep(1)
name = input("Ваше имя: ")
races=["эльф", "гном", "человек", "хобит"]
jobs = ["лучник", "целитель", "воин", "маг"]
enemies = ["хиличурл", "пустынник", "похититель сокровищ", "волк разрыва", "плесенник"]
weapon = ["меч", "лук", "катализатор", "копье", "двуручный меч"]
defense = ["яшмовый щит", "элементальный щит", "пылающий щит", "полог сновидений", "морозный щит"]
powers = ["замораживание", "поджигание", "отравление", "лечение"]
weapon_dict = {1: "обычный", 2: "редкий", 3: "эпический", 4: "легенданый", 5: "хроматический"}
defense_dict = {1: "обычный", 2: "редкий", 3: "эпический", 4: "легенданый", 5: "хроматический"}
food_dict = {4: "лапша", 5: "котлеты", 6: "суп"}
race = input(f"Ваша раса: {races}")
job = input(f"Ваша профессия: {jobs}")
hero = Player.create_player(name, race, job)
print(hero.name, hero.hp, hero.damage)
while True:
    event = random.randint(1, 2)
    if event == 1:
        print("Никто не пришел")
        time.sleep(1)
    elif event == 2:
        enemy = Enemy.enemy_create()
        print(f"Вы встретили {enemy.name}, hp = {enemy.hp}, dmg = {enemy.damage}")
        print(f"У {hero.name}, hp = {hero.hp}, dmg = {hero.damage}, lvl = {hero.level}, exp = {hero.exp}")
        time.sleep(2)
        choice()





