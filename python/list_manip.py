input_nums = input('Enter space separated list of numbers: ').split()

list_nums = [float(num) for num in input_nums]

total = sum(list_nums)

avg = total / len(list_nums)

print(f"Sum of number: {total}")

print(f"Average of number: {avg}")