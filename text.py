# Class


class animals():
  food_eaten = 0
  

class birds(animals):
  eggs = 0
  def harvest_egg(self):
    self.eggs += value
    if self.eggs <= 4:
      print("Вы не у всех собрали яйца")
    elif self.eggs >= 4:
      print("Mission complete!!!")
    print(self.eggs)

 
    



class ducks(animals):
  voice = "Кря-кря"
  def feed_ducks(self, value):
    self.after = self.food_eaten + value
    if self.after <= 100:
      print("Животные остались голодными. Пожалуйста, добавьте корма")
    elif self.after >= 100:
      print("Вы очень внимательны! Гуси и утка накормлены")

class duck_1(ducks):
  name = "Кряква"
  weight = 1 #kg

class duck_2(ducks):
  name  ="Серый"
  weight = 0,689 #kg

class duck_3(ducks):
  name = "Белый"
  weight = 1,2 #kg

  

class chikens(birds):
  voice = "Ко-ко-ко"

  def feed_chikens(self, value):
    self.after = self.food_eaten + value
    if self.after <= 60:
      print("Животные остались голодными. Пожалуйста, добавьте корма")
    elif self.after >= 60:
      print("Вы очень внимательны! Куры накормлены")

class chiken_1(chikens):
  name = "Ko-ko"
  weight = 0,600 #kg

class chiken_2(chikens):
  name = "Кукареку"
  weight = 1,1 #kg
 

class cow(animals):
  voice = "му-му"
  name = "Манька"
  weight = 120 #kg
  food_eaten = 0
  all_milk = 100

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

class sheeps(animals):
  voice = "Бееееее"

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


  

class sheep_1(sheeps):
  name = "Барашек"
  weight = 30 #kg

class sheep_2(sheeps):
  name = "Кудрявый"
  weight = 43 #kg

class goats(animals):
  voice = "Мееее"
  all_milk1 = 70
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
   

class goat_1(goats):
  name_1 = "Рога"
  weight_1 = 51 #kg
  

class goat_2(goats):
  name_2 = "Копыта"
  weight_2 = 33 #kg



def main():
  while True:
    main_input = input("Что вы хотите сделать на ферме?")
    if main_input == "покормить":
      feed_input = input("Кого? Корову, овец, коз, гусей, кур")
      value = int(input("Сколько"))
      if feed_input == "корову":
        cow.feed_cow(cow,value)
      elif feed_input == "овец":
        sheeps.feed_sheeps(sheeps, value)
      elif feed_input == "коз":
        goats.feed_goats(goats, value)
      elif feed_input == "гусей":
        ducks.feed_ducks(ducks, value)
      elif feed_input == "кур":
        chiken.feed_chikens(chiken, value)
      else:
        print("Введите значение на русском и с маленькой буквы")
    elif main_input == "подоить":
      milk_input = input("Кого будете доить? корову или козу")
      milk_time = int(input("А как долго?"))
      if milk_input == "корову":
        cow.milk_cow(cow, milk_time)
      elif milk_input == "коз":
        goats.milk_goats(goats, milk_time)
      else:
        print("Введите значение на русском и с маленькой буквы")
    elif main_input == "подстричь":
      print("Подстричь можно только овец")
      sheeps.trim_sheeps(sheeps)


      




p = main()
