# Уровень здоровья персонажа не может превышать 100ед.
class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.__hp = 100

    def sayHi(self, name, lastname):
        #print("Привет "+name+", меня зовут "+self.name)
        print(f"Привет {name} {lastname}, меня зовут {self.name}")
    def get_private_hp(self): # Геттер
        return self.__hp
    def set_private_hp(self, value): # Сеттер
        if self.__hp+value >= 100:
            self.__hp = 100
        else:
            self.__hp += value

person1 = Person("Иван", "Иванов", 30)
person2 = Person("Алекс", "Александров", 30)
person3 = Person("Вася", "Пупкин", 25)
medKit = 5000
print(person1.get_private_hp())
person1.set_private_hp(-30)
print(person1.get_private_hp())
person1.set_private_hp(medKit)
print(person1.get_private_hp())