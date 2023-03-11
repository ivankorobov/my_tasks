def print_tax_doc(tax, *args, **kwargs):
    price_sum = 0
    for i in args:
        price_sum = price_sum + i * tax / 100
    print("сумма цен с учетом налога:", price_sum)

    for key, value, in kwargs.items():
        print(f"{key}: {value}")

my_tax = int(input("Введите величину налога: "))
print_tax_doc(my_tax, 1000, 900, 800, 700, 600,
              year=1997, doc_tupe="Report", operation_id=92837465
              )
