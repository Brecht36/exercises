# Write your code here
import re
def is_valid_password(string):
    conditions = [
        r'.{12,}',
        r'[a-z]+',
        r'[A-Z]+',
        r'[0-9]+',
        r'[-+/.*@]+'
    ]

    conditions_negative = [
        r'(.)\1{2}',
        r'(.)(.*\1){3}'

    ]
    for regex in conditions:
        if not re.search(regex, string):
            return False
        
    for regex in conditions_negative:
        if re.search(regex, string):
            return False
    

    return True