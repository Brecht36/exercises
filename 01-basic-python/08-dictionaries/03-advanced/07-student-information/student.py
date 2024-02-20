# Write your code here
def process_data(string_data):
    students = {}
    for item in string_data:
        name, age, *courses = item.split(',')
        students[name] = {
            'age': int(age),
            'courses': courses
        }
    return students
    

process_data(['John Smith,20,Math,Physics', 'Jane Doe,21,Biology,Chemistry,Math'])





'''
def average_age(data):
    return data

def courses(data):
    return data

def most_common_course(data):
    return data
'''
