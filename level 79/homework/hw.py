# მთელი რიცხვი(integer)
age = 20
# ათწილადი რიცხვი(float)
height = 1.82
# სიმბოლო(Character - python-ში უბრალოდ სტრინგია ერთ სიმბოლოდ)
grade = 'S'
# ტექსტი(string)
name = "სანდრო"
# ლოგიკური მნიშვნელობა(Boolean)
is_student = True
# მცირე მთელი რიცხვი(python-ში ტიპი ავტომატურად განისაზღვრება)
level = 5 # იგივენაირად წერია, მაგრამ შესაძლოა byte-ს როლი ჰქონდეს
# გრძელი მთელი რიცხვი(long - python-ში უბრალოდ int)
population = 7800000000
# მცურავი წერტილით რიცხვი(float)
temperature = 36.6
# მოკლე მთელი რიცხვი(short - python-ში ისევ int)
year = 20025
# უჭურველი სიმბოლო(Unsigned int - python-ში პირდაპირ არ არესბობს მაგრამ გამოიყენება ჩვეულებრივი int)
score = 150

# მონაცემების გამოტანა
print("სახელი:",name)
print("ასაკი:",age)
print("სიმაღლე:",height)
print("შეფასება:",grade)
print("სტუდენტია:",is_student)
print("დონე:",level)
print("მოსახლეობა:",population)
print("ტემპერატურა:",temperature)
print("წელი:",year)
print("ქულა:",score)


# 11 მომხამრებელს შეყვანინოს თარიღი და შეამოწმოს ფარული თუ არა (ამაში ალბათ წელი იგულისხმება და ნაკნიანი წელი)
year = int(input(" შეიყვანე წელი: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
   print("ეს ნაკიანი წელია.")
else:
    print("ეს არ არის ნაკიანი წელი.")

# 12 მომხმარებელს შეაყვანინე ორი რიცხვი და დაბეჭდე უმცირესი
num1 = int(input("შეიყვანე პირველი რიცხვი: "))
num2 = int(input("შეიყვანე მეორე რიცხვი: "))
print("უმცირესი რიცხვი არის:", min(num1, num2))

# 13 მომხმარებელს შეაყვანინე ასაკი და დაადგინე ასაკობრივი კატეგორია
age = int(input("შეიყვანე ასაკი"))
if age < 13:
    print("ბავშვი")
elif age < 18:
    print("მოზარდი")
elif age < 60:
    print("ზრდასრული")
else:
    print("ხანდაზმული")

# 14 მომხმარებელს შეაყვანინე 2 რიცხვი და შეასრულე 5 სხვადასხვა მათემატიკური ოპერაცია
a = float(input("შეიყვანე რიცხვი A: "))
b = float(input("შეიყვანე რიცხვი B: "))
print("შეკრება:",a + b)
print("გამოკლება:",a - b)
print("გამრავლებ:ა",a * b)
print("გაყოფა:",a / b if b != 0 else "ნულზე გაყოფა შეუძლებელია")
print("ნაშთით გაყოფა:",a % b if b != 0 else "ნულზე ნაშთით გაყოფა შეუძლებელია ")

# 15 მომხმარებელს შეაყვანინე რიცხვი და დაბეჭდე მისი გამრავლების ტაბულა 1-დან 10-მდე
number = int(input("შეიყვანე რიცხვი გამრავლების ტაბულისთვის:"))
for i in range(1, 11):
    print(f"{number} x {i} = {number * i} ")

# 16 მომხმარებელი შეიყვანს რიცხვს და პროგრამამ უნდა განსაზღვროს ლუწია თუ კენტი
num = int(input("შეიყვანე რიცხვი:"))
if num % 2 == 0:
    print("ეს რიცხვი ლუწია.")
else:
    print("ეს რიცხვი კენტია.")

# 17 მომხმარებელი შეიყვანს რიცხვს პროგრამამ უნდა შეამოწმოს არის თუ არა 5-ის ჯერადი
x = int(input("შეიყვანე რიცხვი"))
if x % 5 == 0:
    print("ეს რიცხვი 5-ის ჯერადია.")
else:
    print("ეს რიცხვი არ არის 5-ის ჯერადი.")

# 18 მომხმარებელს შეაყვანინე მისი ასაკი და დაბეჭდოს შეტყობინება:
# თუ ასაკი ნაკლებია 18-ზე: "თქვენ არასრულწლოვანი ხართ"
# თუ მეტია ან ტოლია 18: "თქვცენ ხართ სრულწლოვანი"
age_check = int(input("შეიყვანე შენი ასაკი :"))
if age_check < 18:
    print("თქვენ არასრულწლოვანი ხართ.")
else:
    print("თქვენ ხართ სრულწლოვანი.")


# 19
my_name = "sandro" # აქ ჩაწერე შენი სახელი

user_name = input("შეიყვანე შენი სახელი:")

if len(user_name) == len(my_name):     
   print("ჩვენ სახელებში ერთნაირი რაოდენობის ასოებია")
else:
    print("კარგი სახელია") 

# 20
num = int(input("შეიყვანე რიცხვი"))
if num % 2 == 0:
   print("ლუწია")  
else:
    print("კენტია")

# 21 
a = float(input("შეიყვანე პირველი რიცხვი: "))
b = float(input("შეიყვანე მეორე რიცხვი: "))
op = float(input("მოქმედება (+, -, *, /): "))

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    if b != 0:
        print(a / b)
    else:
        print("ნულზე გაყოფა არ შეიძლება")
else:
    print("არასწორი ოპერაცია")


# 22
book = input("რომელი წიგნი გირჩევნია? ")
if book. lower() == "ჰარი პოტერი":
    print("ეს არის მაგიური წიგნი")
else:
    print("შეყვანილია სხვა წიგნი")

# 23
print(False or True) # შედეგი იქნება: True

# 24
print(False or True) # შედეგი იქნება: False

# 25
print(False and (True or True)) # შედეგი იქნება: False

# 26
print((True and False) or True and True or False)
# True and false -> False
# False or True and True -> True and True -> True
# საბოლოო შედეგი: True

# 27
print(False or True or True or False and False or (True and False))
# true or False or True False and False or False
# True or False or False -> True

# 28
print(True and(True or False) and False or(True and False)) # პასუხი: False

# 29
name = input("შეიყვანე შენი სახელი:")
if len(name) > 6:
    print("კარგი სახელია.")
else:
    print("მოკლე სახელია.")

# 30
a = int(input("შეიყვანე პირველი რიცხვი: "))
b = int(input("შეიყვანე მეორე რიცხვი: "))

if a < b:
    print("პირველი რიცხვი მეტია მეორე რიცხვზე.")
else:
    print("მეორე რიცხვი მეტია პირველზე.")