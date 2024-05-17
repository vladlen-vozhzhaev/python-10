import math
i = 1
j = 5
while i<13:
    print(" "*j+"*"*i)
    i += 2
    j -= 1

#      *
#     ***
#    *****
#   *******
#  *********
# ***********

# найти максимальный нечётный элемент списка
# nums = [-234,-123,-366,-363,-154,-234]
# max = -math.inf
# for num in nums:
#     if max < num and num % 2 != 0:
#         max = num
# print(max)
# marks = [5,5,4,4,5,5,5,4]
# sum = 0
# for mark in marks:
#     sum += mark
# result = sum / len(marks);
# print(result)
# print(round(result))

# cars = ["bmw", "audi", "kia"]
# for car in cars:
#     print(car)
#

# cars = []
# i = 0
# car = input("Введите марку автомобиля, или exit для выхода из программы: ")
# while car != "/exit": # length
#     cars.append(car)
#     car = input("Введите марку автомобиля, или exit для выхода из программы: ")
#
# print(cars)


# i = 0;
# while i<3:
#     print(f"Hello world {i}")
#     i += 1 # i = i + 1