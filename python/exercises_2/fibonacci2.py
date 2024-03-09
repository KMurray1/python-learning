def fibonacci(x):
    fib_list = [0, 1]
    counter = 2
    while counter < x:
        fib_value = fib_list[counter-2] + fib_list[counter-1]
        fib_list.append(fib_value)
        counter += 1
    return fib_list

if __name__ == '__main__':
    terms = 12
    fib_sequence = fibonacci(terms)
    print(terms, "number of terms fibonacci sequence: ", fib_sequence)