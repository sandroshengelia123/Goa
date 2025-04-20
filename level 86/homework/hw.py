# 1
def merge_and_clean_duplicates(list1, list2):
    merged = list1 + list2                           # ვაერთიანებთ ორ სიას
    cleaned = list (set(merged))                     # ვაშორებთ დუპლიკატებს set-ით და ვაბრუნებთ list-ად
    if cleaned:
        return cleaned                               # თუ სია ცარიელი არ არის, ვაბრუნებთ მას
    else:
        return "სიაში ელემენტები არ მოიძებნა"        # თუ სია ცარიელია


# 2
def prime_numbers_in_range(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
            return True
    
    return [n for n in range(start, end + 1) if is_prime(n)] # ყველა მარტივი რიცხვი მითითებულ დიაპაზონში


# 3
def age_group(age):
    if age < 0:
        return "არასწორი ასაკი"
    elif age < 13:
        return "ბავშვი"
    elif age < 18:
        return "თინეიჯერი"
    elif age < 65:
        return "ზრდასრული"
    else:
        return "ხანდაზმული"
    

# 4
def list_methods_demo():
    my_list = [10, 20, 30]

    my_list.append(40)             # ბოლოში ამატებს 40 -> [10, 20, 30, 40]
    my_list.insert(1, 15)          # ინდექსზე 1 ჩასვამს 15-ს -> [10, 15, 20, 30, 40]
    my_list.pop()                  # შლის ბოლო ელემენტებს (40) -> [10, 15, 20, 30]
    my_list.remove(15)             # შლის პირველივე 15-ს -> [10, 20, 30]

    return my_list


# 5
def min_elements(list1, list2):
    if not list1 or not list2:
        return "ორივე სიაში უნდა იყოს მინიმუმ ერთი ელემენტი"
    
    min1 = min(list1)
    min2 = min(list2)

    return [min1, min2]


# 6
def person_info():
    name = input("შეიყვანე სახელი: ")
    surname = input("შეიყვანე გვარი: ")
    age = int(input("შეიყვანე ასაკი: "))

    full_name = f"{name}  {surname}"
    status = "სრუწლოვანი" if age >= 18 else "არასრუწლოვანი"

    return f"{full_name} არის {status}"

# 7
def person_details():
    name = input("შეიყვანე სახელი: ")
    surname = input("შაიყვანე გავრი: ")
    age = int(input("შეიყვანე სიმაღლე (სანტიმეტრებში): "))
    height_cm = float(input("შეიყვანე სიმაღლე (სანტიმეტრებით): "))
    
    height_m = height_cm / 100

    result = "ჩემი სახელი არის {0}, ჩემი გვარია {1}, მე ვარ {2} წლის და ჩემი სიმაღლეა {3:.2f}მ".format(
        name, surname, age, height_m
    )

    return result