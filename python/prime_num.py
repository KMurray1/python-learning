input_num = int(input('Enter number: '))

def is_prime(number):
    if number <= 1:
        return False
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
            
if is_prime(input_num):
    print('Is Prime')
else:
    print('Not a prime boss!')