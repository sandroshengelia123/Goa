# 1 
def insert_my_name(name_list):
    my_name = "ს.შ" # ჩაწერე შენი სახელი ან ინიციალები
    name_list.insert(3, my_name)
    return name_list

names = ["ნინო," "გიორგი," "სოფო," "სანდრო,"]
updated = insert_my_name(names)
print(updated)

# 2
def insert_my_name(name_list):
    my_name = "ს.შ" # ჩაწერე შენი სახელი ან ინიციალები
    name_list.insert(3, my_name)
    return name_list

def reverse_string(name):
    return name[::-1]


# 3
def remove_digits_from_string(text):
    return ''.join([char for char in text if not char.isdigt()])

result = remove_digits_from_string("ale4qs6and3re")
print(result)
