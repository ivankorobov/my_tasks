def numbers_from_text(text):
    return [int(number) for number in text.rstrip().split()]

def file_parcer(path_to_file):
    with open(path_to_file) as file:
        for line in file:
            # clean_line_sum = sum(numbers_from_text(line))
            clean_line_sum = sum(map(int, line.rstrip().split()))
            yield clean_line_sum


all_sum = 0
for number in file_parcer("numbers.txt"):
    all_sum += number
