# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
def fibonacci(number): # 3
    if number <= 0:
        return 0
    elif number == 1:
        return 1
    else: 
        return fibonacci(number - 1) + fibonacci(number - 2)

print(fibonacci(8))