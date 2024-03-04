def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

number = int(input('Enter number: '))
result = factorial(number)

print(f"Factorial of {number} is {result}")