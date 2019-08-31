def print_triangle(base):
    height = base
    if not 0 < base or not base < 10:
        raise ValueError('input tidak sesuai')
    for digit in range(height):
        prime_found = 0
        prime_candidate = 2
        while not prime_found == digit+1:
            if is_prime_number(prime_candidate):
                prime_found += 1
                print(prime_candidate, end=' ')
            prime_candidate += 1
        print('')


def is_prime_number(x):
    if x >= 2:
        for y in range(2, x):
            if not (x % y):
                return False
    else:
        return False
    return True


print_triangle(5)
