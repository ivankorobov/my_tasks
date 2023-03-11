class CountIterator:
    count = 0

    def __iter__(self):
        return self

    def __next__(self):
        CountIterator.count += 1
        return CountIterator.count - 1



my_iter = CountIterator()
for i_elem in my_iter:
    print(i_elem)
