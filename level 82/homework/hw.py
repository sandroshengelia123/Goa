def dont_give_me_five(start, end):
    count = 0
    for i in range(start, end + 1):
        if '5' not in str(i):
            count += 1
    return count

# ტესტები
print(dont_give_me_five(1, 9))
print(dont_give_me_five(4, 17))
print(dont_give_me_five(50, 60))




# test
#print(small_enough([66, 101,], 200)) # true
#print(small_enough([78, 117, 110, 99, 104],)) # false
#print(small_enough([] 100)) # true





#print(add_length("apple ban")) # Output: ['apple 5', 'ban 3']
#print(add_length("you will win")) # Output:['you 3', 'will 4', 'win 3']



#def sum_mix(arr):
    #return sum(int(x) for x in arr


# test
#print(sum_mix([9, 3, '7', '3'])) # 22
#print(sum_mix(['5', 0, 3, 2, 1, '9', 6, 7])) # 42