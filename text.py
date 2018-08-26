# -*- coding: utf-8 -*-
class Animals():
    food_eaten = 0


class Birds(Animals):
    eggs = 0

    def harvest_egg(self, value):
        self.eggs += value
        if self.eggs <= 4:
            print("Вы не у всех собрали яйца")
        elif self.eggs >= 4:
            print("Mission complete!!!")
        print(self.eggs)


class Ducks(Birds):
    def __init__(self, n, w, v):
        self.name = n
        self.weight = w
        self.voice = v
        print(n, w, v)

    def feed_ducs(self, value):
        self.after = self.food_eaten + value
        if self.after <= 60:
            print("Животные остались голодными. Пожалуйста, добавьте корма")
        elif self.after >= 60:
            print("Вы очень внимательны! Куры накормлены")


duck_1 = Ducks("Кряква", "1,26kg", "Кря-кря")
duck_2 = Ducks("Серый", "2kg", "Кря-кря")
duck_3 = Ducks("Белый", "2,56kg", "Кря-кря")


class Chiсkens(Birds):
    def __init__(self, n, w, v):
        self.name = n
        self.weight = w
        self.voice = v
        print(n, w, v)

    def feed_chiсkens(self, value):
        self.after = self.food_eaten + value
        if self.after <= 60:
            print("Животные остались голодными. Пожалуйста, добавьте корма")
        elif self.after >= 60:
            print("Вы очень внимательны! Куры накормлены")


Chiсken_1 = Chiсkens("Ko-ko", "0,6kg", "Ко-ко-ко")
Chiсken_2 = Chiсkens("Кукареку", "1,1kg", "Ко-ко-ко")


class Cow(Animals):
    all_milk = 100

    def __init__(self, n, w, v):
        self.name = n
        self.weight = w
        self.voice = v
        print(n, w, v)

    def feed_cow(self, value):
        self.after = self.food_eaten + value
        if self.after <= 250:
            print("Животное осталась голодным. Пожалуйста, добавьте корма")
        elif self.after >= 250:
            print("Вы очень внимательны! Животное накормлено")

    def milk_cow(self, value):
        self.all_milk -= value
        if self.all_milk <= 0:
            print("Замечательно! Вы подоили корову Маньку")
        elif self.all_milk >= 0:
            print("Увы, но молоко у коровы ещё осталось, нужно доить дальше")

cow_1 = Cow("Манька", "146kg", "му-му")


class Sheeps(Animals):

    def __init__(self, n, w):
        self.name = n
        self.weight = w
        print(n, w)

    def feed_sheeps(self, value):
        self.after = self.food_eaten + value
        if self.after <= 150:
            print("Животные остались голодными. Пожалуйста, добавьте корма")
        elif self.after >= 150:
            print("Вы очень внимательны! Барашки накормлены")

    def trim_sheeps(self):
        answer = input("Кого вы будете стричь, Барашка или Кудрявого?")
        if answer == "Барашка":
            print("Ура! Барашек подстрижен")
        elif answer == "Кудрявый":
            print("Ура! Кудрявый подстрижен")


sheep_1 = Sheeps("Барашек", "30kg")
sheep_2 = Sheeps("Кудрявый", "42kg")


class Goats(Animals):
    all_milk1 = 70

    def __init__(self, n, w, v):
        self.name = n
        self.weight = w
        self.voice = v
        print(n, w, v)


    def feed_goats(self, value):
        self.after = self.food_eaten + value
        if self.after <= 150:
            print("Животные остались голодными. Пожалуйста, добавьте корма")
        elif self.after >= 150:
            print("Вы очень внимательны! Козы накормлены")

    def milk_goats(self, value):
        self.all_milk1 -= value
        if self.all_milk1 <= 0:
            print("Замечательно! Вы подоили коз")
        elif self.all_milk1 >= 0:
            print("Увы, но молоко у кого-то осталось, нужно доить дальше")


goat_1 = Goats("Рога", "24kg", "Мееее")
goat_2 = Goats("Копыта", "35kg", "Мееее")


def main():
    while True:
        main_input = input("Что вы хотите сделать на ферме?")
        if main_input == "покормить":
            feed_input = input("Кого? Корову, овец, коз, гусей, кур")
            value = int(input("Сколько"))
            if feed_input == "корову":
                Cow.feed_cow(Cow, value)
            elif feed_input == "овец":
                Sheeps.feed_sheeps(Sheeps, value)
            elif feed_input == "коз":
                Goats.feed_goats(Goats, value)
            elif feed_input == "гусей":
                Ducks.feed_ducks(Ducks, value)
            elif feed_input == "кур":
                Chiсkens.feed_chiсkens( Chiсkens, value)
            else:
                print("Введите значение на русском и с маленькой буквы")
        elif main_input == "подоить":
            milk_input = input("Кого будете доить? корову или козу")
            milk_time = int(input("А как долго?"))
            if milk_input == "корову":
                Cow.milk_cow(Cow, milk_time)
            elif milk_input == "коз":
                Goats.milk_goats(Goats, milk_time)
            else:
                print("Введите значение на русском и с маленькой буквы")
        elif main_input == "подстричь":
            print("Подстричь можно только овец")
            Sheeps.trim_sheeps(Sheeps)


p = main()

