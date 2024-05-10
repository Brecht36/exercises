def reverse_from_left(text):
    # Base case:
    if len(text) <= 1:
        return text
    # Recursive case: 
    else:
        return reverse_from_left(text[1:]) + text[0]

def reverse_from_right(text):
    # Base case:
    if len(text) <= 1:
        return text
    # Recursive case: 
    else:
        return text[-1] + reverse_from_right(text[:-1])