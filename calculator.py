#This is a calculator
import math

def sine(value):
    return math.sin(value)

def cosi(value):
    return math.cos(value)

symbol = input('Enter your equation: ')
if '/' in symbol:
    numbers = symbol.split('/')
    print(numbers)
    res = float(numbers[0])
    for i in range(0, len(numbers)-1):
        res = res / float(numbers[i+1])
    print(res)  
        
elif '*' in symbol:
    numbers = symbol.split('*')
    print(numbers)
    res = float(numbers[0])
    for i in range(0, len(numbers)-1):
        res = res * float(numbers[i+1])
    print(res)
    
elif '+' in symbol:
    numbers = symbol.split('+')
    print(numbers)
    res = float(numbers[0])
    for i in range(0, len(numbers)-1):
        res = res + float(numbers[i+1])
    print(res)
    
elif '-' in symbol:
    numbers = symbol.split('-')
    print(numbers)
    res = float(numbers[0])
    for i in range(0, len(numbers)-1):
        res = res - float(numbers[i+1])
    print(res)

elif 'cosine' in symbol:
    value = symbol.split("(")[1].split(")")
    print(cosi(float(value[0])))
    
elif 'sine' in symbol:
    value = symbol.split("(")[1].split(")")
    print(sine(float(value[0])))


