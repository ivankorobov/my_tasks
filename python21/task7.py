# def my_func(num,
#             lst=[]):
#     lst.append(num)
#     print(lst)
#
# my_func(5)
# my_func(10)
# my_func(15)

def add_num(num, nums=None):
    nums = nums or []
    # хитрая конструкция, которая позволит упростить ввод:
    # if not nums:
    #    nums = []
    # Первый вариант будет выбран, если nums не равен None, иначе будет создан и записан пустой список
    nums.append(num)
    print(nums)


add_num(5)

add_num(10)

add_num(15)