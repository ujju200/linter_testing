import os
import sys
import json  # Unused import

def calculateSum(numbers):  # Naming convention: should be calculate_sum
    x = 0  # Vague variable name
    for i in range(len(numbers)):  # Should use enumerate or direct iteration
        x = x + numbers[i]
    return x

def process_data(data):
    password = "admin123"  # Hardcoded credential - SECURITY ISSUE
    
    if data == None:  # Should use 'is None'
        return False
    
    try:
        result = int(data)
    except:  # Bare except clause - too broad
        pass  # Empty except block
    
    return result  # 'result' may be undefined if exception occurs

def divide(a, b):
    result = a / b  # No check for division by zero
    return result

class myClass:  # Class naming: should be MyClass
    def __init__(self):
        self.value = 1
    
    def getValue(self):  # Method naming: should be get_value
        return self.value
    
    def setValue(self, v):  # Method naming: should be set_value
        self.value = v

def duplicate_code_1(items):
    total = 0
    for item in items:
        total = total + item
    print("Total:", total)
    return total

def duplicate_code_2(items):  # Duplicated logic
    total = 0
    for item in items:
        total = total + item
    print("Total:", total)
    return total

def too_complex(a, b, c, d, e, f):  # High cognitive complexity
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        if f > 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

API_KEY = "sk-1234567890abcdef"  # Hardcoded secret - SECURITY ISSUE

def sql_query(user_input):
    query = "SELECT * FROM users WHERE name = '" + user_input + "'"  # SQL Injection vulnerability
    return query

def open_file():
    f = open("test.txt", "r")  # File not closed / no context manager
    data = f.read()
    return data

# Dead code - unreachable
def unreachable():
    return 1
    print("This will never execute")  # Unreachable code

if __name__ == "__main__":
    print(calculateSum([1, 2, 3]))
