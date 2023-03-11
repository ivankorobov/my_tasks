import random
arr1 = [random.randint(50, 80) for _ in range(10)]
arr2 = [random.randint(30, 60) for _ in range(10)]
arr3 = ["Погиб" if arr1[i] + arr2[i] > 100 else "Выжил" for i in range(10)]
print(arr1)
print(arr2)
print(arr3)