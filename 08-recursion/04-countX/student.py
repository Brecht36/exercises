def countX(text):
    if not text:
        return 0
    
    isX = 1 if text[0] == "x" else 0
    
    return isX + countX(text[1:])