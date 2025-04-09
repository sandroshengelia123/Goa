def greet():
    return "hello world!"

# test
print(greet()) # hello world!

def make_upper_case(s):
    return s.upper()

# test
print(make_upper_case("hello")) # -> "hello"
print(make_upper_case("python")) # -> "python"
print(make_upper_case("")) # -> ""

def repeat_str(n, s):
    return s * n

# test
#print(repeat_str("3, "hi")) # "hihihi"
#print(repeat_str(0, "bye")) # ""
#print(repeat_str(2, "abc")) # "abc abc"


def no_space (x):
    return x.replace(" ", "")

# test
print(no_space("8 j 8 mBliB8g  imjB8B8  jl B")) # "8j8mBliB8gimjB8B8jlB"
print(no_space("      hello world    ")) # "helloworld"
print(no_space("")) # ""

def create_array(n):
    return [i for i in range(n)]

# test
print(create_array(5)) # [0, 1, 2, 3, 4]
print(create_array(0)) # []
print(create_array(1)) # [0]


def maps(a):
    return [x* 2 for x in a]

# test
print(maps([1, 2, 3])) # [2, 4, 6]
print(maps([4, 1, 1, 4])) # [8, 2, 2, 2, 8]
print(maps([])) # []

def basic_op(operator, value1, value2):
    if operator == '+': # <- ახლა სწორია
        return value1 + value2
    
# test
print(basic_op("+", 4, 7)) # 11
print(basic_op("-", 15, 18 )) # -3
print(basic_op("*", 5, 5)) # 25
print(basic_op("/", 49, 7 )) # 7.0
