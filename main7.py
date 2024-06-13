nums = []

num = 1
for i in range(3):
    nums.append([])
    for j in range(3):
        nums[i].append(num)
        num += 1

result = ""
for i in range(len(nums)):
    for j in range(len(nums[i])):
        result += str(nums[i][j])

print(result)
# nums = [
#     [4,6],
#     [7,4,2],
#     [8,2,7]
# ]
#
# max = 0
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         if nums[i][j] > max:
#             max = nums[i][j]
#
# print(max)
# summ = 0
# for i in range(len(nums)):
#     for j in range(len(nums[i])):
#         summ += nums[i][j]
#
# print(summ)
# arr1 = []
# def calc(t):
#     arr1.append([2*t**2, 4*t, 4])
#
# for i in range(11):
#     calc(i)
#
# print(arr1)

 # arr = [43, 12, 23, 231, 6, 9]
# print( sorted(arr) )

 # arr2 = [x for x in arr if x%2 == 0]

# for i in range( len(arr) ):
#     if arr[i]%2 == 0:
#         arr2.append(arr[i])
# def quick_sort(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quick_sort(left) + middle + quick_sort(right)