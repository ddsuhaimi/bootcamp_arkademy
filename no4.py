import itertools


def split_and_sort(number):
    portions = str(number).split('0')
    sorted_portions = []
    for portion in portions:
        digit = [int(i) for i in portion]
        digit.sort()
        sorted_portions.append(digit)

    sorted_digit = []
    for i in sorted_portions:
        for j in i:
            sorted_digit.append(j)

    result = ''.join([str(x) for x in sorted_digit])
    return int(result)


print(split_and_sort(5956560159466056))
