def power(a, n):
    if n <= 0:
        return 1

    result = power(a, n - 1)

    return a * result


float_num = float(input('Введите вещественное число: '))

int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))