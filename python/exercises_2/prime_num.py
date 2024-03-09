def is_prime(x):
    if x <= 1:
        return False
    for i in range(2,x):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':
    value = 149
    if is_prime(value):
        print('is prime bruv')
    else:
        print('not a prime g')