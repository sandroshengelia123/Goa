def get_count(s):
    ls = ["a","o","i","e","u"]
    count = 0
    for i in s:
        if i in ls:
            count+=1
    return count


def high_and_low(n):
    n = n.split(" ")
    ls = []
    for i in n:
        ls.append(int(i))
    return f"{max(ls)} {min(ls)}"


def find_short(s):
    n = s.split(" ")
    ls = []
    for i in n:
        ls.append(len(i))
    return min(ls)


def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]