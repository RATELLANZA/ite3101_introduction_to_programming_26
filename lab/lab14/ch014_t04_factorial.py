def factorial(x:int)->int:
    value = 0
    for i in range(1, x+1):
        value *= i
    return value