#arr = [43, 12, 23, 231, 5, 9]
arr = ["б", "я", "Ц", "А", "Я", "ав", "аб", "к"]
print("Исходный список", arr)

def selection_sort(arr):
    n = len( arr )
    for i in range(n):
        minIndex = i
        for j in range(i+1, n):
            if arr[j] < arr[minIndex]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
        print(arr)
    return arr

result = selection_sort(arr)
print("Результат: ", result)

# Напишите программу, которая создает двумерный массив размером 3x3 и заполняет его числами от 1 до 9.
# Затем программа должна выводить строку из элементов каждой строки массива.