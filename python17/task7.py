import random
original_prices = [-12, 3, 5, -2, 1]
    # [random.randint(-50, 50) for _ in range(10)]
new_prices = original_prices[:]

for i in range(len(original_prices)):
    if new_prices[i] < 0:
        new_prices[i] = 0

print("Мы потеряли: ",  sum(original_prices) - sum(new_prices))