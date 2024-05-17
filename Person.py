class Person:
    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    def sayHi(self, name, lastname):
        #print("Привет "+name+", меня зовут "+self.name)
        print(f"Привет {name} {lastname}, меня зовут {self.name}")

person1 = Person("Иван", "Иванов", 30)
person2 = Person("Алекс", "Александров", 30)
person3 = Person("Вася", "Пупкин", 25)

person3.sayHi( person1.name, person1.lastname )
person2.sayHi( person1.name, person1.lastname )