arr = ["б", "я", "Ц", "А", "Я", "ав", "аб", "к"]
print("Исходный список", arr)

def insertion_sort(arr):
    n = len( arr )
    for i in range(1, n):
        number = arr[i]
        j = i - 1
        while j >= 0 and number < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = number
    return arr

result = insertion_sort(arr)
print("Результат: ", result)