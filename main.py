class Vorior():
    def __init__(self, name, power, endurance, hair_color):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color
    def sleep(self):
        print(f"{self.name} спит!")
        self.endurance += 2

    def eat(self):
        print(f"{self.name} сел кушать")
        self.power += 1

    def hit(self):
        print(f"{self.name} бьет когото")
        self.endurance -= 6

    def walk(self):
        print(f"{self.name} гуляет")

    def info(self):
        print(f" Имя воина {self.name}")
        print(f" Сила воина {self.power}")
        print(f" Выносливость воина {self.endurance}")
        print(f" Цвет волос воина {self.hair_color}")


var1 = Vorior("Стёпа", 60, 78, "Коричневый")
var2 = Vorior("Егор", 15, 60, "Белый")

var1.sleep()
var1.eat()
var1.hit()
var1.walk()
var1.info()

var2.sleep()
var2.eat()
var2.hit()
var2.walk()
var2.info()


