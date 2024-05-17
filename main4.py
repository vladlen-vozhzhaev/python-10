# Имеется набор букв 'КЛМН',
# 1) необходимо вывести на экран все возможные комбинации 4х символьных слов из этих букв
# 2) все строки должны быть пронумированны
# 3) узнать на какой позиции находится слово 'МЛКН'
# Пример:
# 1) КККК
# 2) КККЛ
# 3) КККМ
# 4) КККН
# 5) ККЛК....

# chars = ['К', 'Л', 'М', 'Н']
# counter = 1
# position = 0
# for char1 in chars:
#     for char2 in chars:
#         for char3 in chars:
#             for char4 in chars:
#                 word = char1+char2+char3+char4
#                 if(word == 'МЛКН'):
#                     position = counter
#                 print(str(counter)+') '+word)
#                 counter += 1
# print('Строка "МЛКН" имеет номер: '+str(position))