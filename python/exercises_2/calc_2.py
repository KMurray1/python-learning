def calculator(x, y, operator):
    if operator == '+':
        return x + y
    if operator == '-':
        return x - y
    if operator == '*':
        return x * y
    if operator == '/':
        return x / y
    else:
        return 'InvalidOperator'


if __name__ == '__main__':
    result = calculator(10,20,'*')
    print("Result: ", result)

