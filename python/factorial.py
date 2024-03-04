number = int(input('Enter number: '))

factorial = 1

for i in range(1,number+1):
    factorial = factorial * i

print(f" Factorial is {factorial}")