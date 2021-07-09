def calculate(a, b, c):
    if a == '+':
        return b + c
    elif a == '-':
        return b - c 
    elif a == '*' or a == 'x':
        return b * c 
    elif a == ':' or a == '/':
        return b / c 
        
number1 = 69 
number2 = 69 
action = '*'

print(calculate(action, number1, number2))
