x = float(input('First number: '))

operator = input('arithmetic operator (+, -, *, /): ')

y = float(input('Second number: '))


if operator == '*':
    multiply = x * y
    print(multiply)

elif operator == '/':
    divide = x / y
    print(divide)

elif operator == '+':
    sum = x + y
    print(sum)

elif operator == '-':
    subtract = x - y
    print(subtract)

else:
    print('invalid')

