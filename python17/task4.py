a = int(input("1е число: "))
b = int(input("2е число: "))
arr = [x for x in range(a, b + 1) if x % 2 == 0]
print(arr)