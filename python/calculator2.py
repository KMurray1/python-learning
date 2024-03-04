x = float(input('First number: '))

operator = input('arithmetic operator (+, -, *, /): ')

y = float(input('Second number: '))


if operator == '*':
    result = x * y

elif operator == '/':
    result = x / y

elif operator == '+':
    result = x + y

elif operator == '-':
    result = x - y

else:
    print('invalid')

print(f"Answer: {result}")