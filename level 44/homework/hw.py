def solution(s):
    return s[::-1]

def century(year):
    count = 0
    while year > 0:
        year -= 100
        count += 1
    return count


def digitize(n):
    n = (str(n))[::-1]
    ls =  []
    for i in n:
        ls.append(int(i))
    return ls


def summation(num):
    sum = 0
    
    for i in range (num+1):
        sum += i
    
    return sum 


def sum_array(a):
    return sum(a)