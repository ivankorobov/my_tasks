number = 1
for i in range(1, 10):
  for k in range(i, i * 10, i):
    print(k, end="\t")
  print()
