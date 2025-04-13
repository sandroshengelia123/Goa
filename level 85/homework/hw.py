#1
num1 = float(input("შეიყვანე პირველი რიცხვი:"))
num1 = float(input("შეიყვანე მეორე რიცხვი:"))
operation = input("აირჩიე მოქმედება (addition, subtraction, multiplaction, division): ")

if operation == "addition":
    #result = num1 + num2
# elif operation == "subtraction":
      #result = num1 - num2
# elif operation == "multiplication":
      # result = num1 * num2
# elif operation == "division":
      #if num2 != 0:
          #result = num1 / num2
#else:
     result = "ნულზე გაყოფა არ შეიძლება "
#else:
     #result = "არსწორი ოპერაციაა"

print("შედეგი:", result)


#2
name = input("შეიყვანე შენი სახელი: ")
surname = input("შეიყვამე შენი გვარი: ")
age = input("შეიყვანე შენი ასაკი: ")

print("ჩემი სახელია", name + ",", "ჩემი გვარი", surname + "და ჩემი ასაკია", age, "წელი.")

#3
name = "sandro"
surname = "shengelia"
age = 17

print(f"ჩემი სახელია {name}, ჩემი გვარია {surname},და მე ვარ {age} წლის")

#4
def calculator():
     num1 = float(input("შეიყვანე პირველი რიცხვი: "))
     num2 = float(input("შეიყვანე მეორე რიცხვი: "))
     operation = input("აირჩიე ოპერაცია (+, -, *, /): ")

     if operation == "+":
         result = num1 + num2
    #elif operation == "-"
          # result = num1 - num2
    #elif operation == "*"
          # result = num1 * num2
    # elif operation == "/"
        # if num2 != 0:
             # result = num1 / num2
        # else:
             #  return "ნულზე გაყოფა არ შეიძლება" 
        # else:
              # return "არასწორი ოპერაცია"
        # return f"შედეგი: {num1} {operation} {num2} = {result}"

# ფუნქციის გამოძახება
print(calculator())

#5
def is_prime(n):
     if n < 2:
          return False
     for i in range(2, int(n**0.5)+1):
          if n % i == 0:
               return False
          return True
     
def sum_of_primes():
     limit = int(input("შეიყვანე რიცხვი"))
     total = 0
     for num in range(2, limit + 1):
         if is_prime(num):
             total += num
   # return f"{limit}-მდე ყველა მარტივი რიცხვის ჯამია: {total}"

# ფუნქციის გამოძახება
print(sum_of_primes ())
     
             