def sum_numbers(number):
    
    number = abs(number)

    # Base case: if the number is a single digit
    if number < 10:
        return number

    # Recursive case: sum the last digit with the sum of the rest
    return (number % 10) + sum_numbers(number // 10)