num_of_terms = int(input('Number of fibonacci terms: '))

fib_list = [0, 1]
fib_value = 1

counter = 2

while counter <= num_of_terms:
    fib_value = fib_list[counter-2] + fib_list[counter-1]
    fib_list.append(fib_value)
    counter += 1

print(fib_list)