limit = 1000


def get_sum_of_multiplies(number):
    i = 1
    sum = 0
    while (number * i) < limit:
        sum += number * i
        i += 1
    return sum


sum = get_sum_of_multiplies(3) + get_sum_of_multiplies(5) - get_sum_of_multiplies(15)
print(sum)
