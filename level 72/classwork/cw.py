def find_multiples(n, limit):
    
    final_list = []

    for i in range(n, limit+1, n):
        final_list.append(i)


        return final_list
    
print(find_multiples(3, 30))