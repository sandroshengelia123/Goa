def bonus_time(salary, bonus):
    return f"${salary * 2 if bonus else salary}"

#print(bonus_time(10000, true))
#print(bonus_time(25000, false))

def century(year):
    return (year + 99) // 100

print(century(1705)) # 18
print(century(1900)) # 19
print(century(1601)) # 17
print(century(2000)) # 20

def maps(a):
    return [x * 2 for x in a]

print(maps([1, 2, 3])) # [2, 4, 6]
print(maps([4, 1, 1, 1, 4])) # [8, 2, 2, 2, 8]
print(maps([])) #[]


def minimum(arr):
    return min(arr)

def maximum(arr):
    return max (arr)

print(minimum([52, 56, 30, 29, -54, 0, -110])) # -110
print(minimum([52, 56, 30, 29, -54, 0, -110])) # 56
print(minimum([5]))                           # 5
print(minimum([5]))                           # 5


def divisible_by(numbers, divisor):
    return [num for num in numbers if num % divisor == 0]

print(divisible_by([1, 2, 3, 4, 5, 6], 2)) # [2, 4, 6]
print(divisible_by([10, 15, 20, 24],  5)) # [10, 15, 20, 25]
print(divisible_by([3, 5, 7,],  2))       # []

