from calc_2 import calculator

x = int(input('First number: '))

y = int(input('Second number: '))

operator = input('Operator: ')

user_result = calculator(x,y,operator)

print('Answer is: ', user_result)