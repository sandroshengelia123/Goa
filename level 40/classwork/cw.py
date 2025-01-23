def greet ():
    return "hello world!"

def hello (name='Hello, World!'):
    
    if name == 'Hello, World!' or name == "":
        return 'Hello, World!'
    else:
        name = (name.lower()).capitalize()
        return f"Hello, {name}!"
    

def multiply(a, b):
    return a * b

def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"