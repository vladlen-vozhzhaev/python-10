# def f(x):
#     return x**2
#
# print( f(1) )
# print( f(2) )
# print( f(-2) )
# print( f(3) )
# print( f(4) )

# def sayHi(name):
#     print("Привет "+name)
#
# sayHi("Иван")
# sayHi("Вася")
# sayHi("Алекс")

# def auth():
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     if login == "admin" and password == "123":
#         print("Доступ разрешен! - ADMIN")
#     elif login == "user" and password == "321":
#         print("Доступ разрешен! - USER")
#     elif login == "superuser" and password == "32111":
#         print("Доступ разрешен! - superuser")
#     else:
#         print("Доступ запрещен!")
#         return False
#     return True
#
#
# while True:
#     if auth(): break
#     else: print("ПОПРОБУЙТЕ ЕЩЁ РАЗ!!!")


# def isAuth():
#     login = input("Enter login: ")
#     password = input("Enter pass: ")
#     if login == 'admin' and password == '123':
#         return True
#     else:
#         return False
#
# if isAuth():
#     print("success")
# else:
#     print("error")

# Имеется кофе автомат, по завершении процесса приготовления кофе автомат выдаёт сдачу
# монетами с номиналом: 1, 2, 5, 10
# Реализовать функцию, которая принимает на вход число(сдача) и печатает на экран сдачу
# Пример:
# 36 = 10 10 10 5 1
# 29 = 10 10 5 2 2

def getChange(num):
    coin = 0
    if num>=10: coin = 10
    elif num>=5: coin = 5
    elif num>=2: coin = 2
    elif num>=1: coin = 1

    if coin > 0:
        print(coin)
        getChange(num - coin)


getChange(36)


# def f(n):
#     if n>2:
#         return g(n-1)+f(n//2)
#     else:
#         return n
#
# def g(n):
#     if n>2:
#         return f(n-1)+g(n%2)
#     else:
#         return 1
#
# print( f(9) )
#
# # f(9) = g(8)+f(4) = 9 + 5 = 14
# # g(8) = f(7)+g(0) = 8 + 1 = 9
# # f(7) = g(6)+f(3) = 6 + 2 = 8
# # g(6) = f(5)+g(0) = 5 + 1 = 6
# # f(5) = g(4)+f(2) = 3 + 2 = 5
# # g(4) = f(3)+g(0) = 2 + 1 = 3
# # f(3) = g(2)+f(1) = 1 + 1 = 2
# # f(4) = g(3)+f(2) = 3 + 2 = 5
# # g(3) = f(2)+g(1) = 2 + 1 = 3

def f():
    print("hello world")
    f()

f()