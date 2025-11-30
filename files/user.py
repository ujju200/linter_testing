import os
import sys
import json
import random

def BadFunctionName(x,y):
    z=x+y
    return z

class user_account:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.password = "password123"
    
    def GetUserInfo(self):
        return self.name + " " + str(self.age)

def process_list(items):
    l = []
    for i in range(len(items)):
        if items[i] != None:
            l.append(items[i])
    return l

def risky_divide(a, b):
    return a/b

def fetch_data(url):
    api_key = "AKIAIOSFODNN7EXAMPLE"
    secret = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
    connection_string = "mysql://root:admin@localhost:3306/db"
    return url + api_key

def unused_variables():
    x = 10
    y = 20
    z = 30
    return x

def no_return_type(flag):
    if flag:
        return "yes"

def broad_exception():
    try:
        file = open("data.txt")
        data = file.read()
    except:
        pass

def sql_builder(username):
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return query

def compare_types(val):
    if type(val) == int:
        return True
    if val == True:
        return "yes"
    if val == None:
        return "none"

def mutable_default(items=[]):
    items.append(1)
    return items

def too_many_args(a, b, c, d, e, f, g, h, i, j):
    return a + b + c + d + e + f + g + h + i + j

DEBUG = True
if DEBUG == True:
    print("Debug mode")

x = lambda a,b: a+b

def deep_nesting(data):
    if data:
        if len(data) > 0:
            if isinstance(data, list):
                if data[0]:
                    if data[0] > 0:
                        return True
    return False
