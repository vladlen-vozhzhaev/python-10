class Animal:
    def __init__(self, nickname, age, breed):
        self.nickname = nickname
        self.age = age
        self.breed = breed
    def run(self):
        print(f"{self.nickname} побежал(а)")
    def speak(self):
        print("Звук не назначен")

class Cat(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
    def speak(self):
        print("Мяу")

class Bird(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)
    def fly(self):
        print(f"{self.nickname} полетел(а)")
    def speak(self):
        print("Чык чырык")

class Horse(Animal):
    def __init__(self, nickname, age, breed):
        super().__init__(nickname, age, breed)

cat1 = Cat("Барсик", 6, "Дворняга", 5)
bird = Bird("Кеша", 3, "Волнистый")
horse = Horse("Мустанг", 4, "Рысак")
print(cat1.a)
cat1.run()
bird.run()
bird.fly()
cat1.speak()
bird.speak()
horse.speak()