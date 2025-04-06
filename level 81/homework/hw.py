# simple calculator

def calculator(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
          return a - b
    elif op == "*":
          return a * b
    elif op == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"
    
# მაგალითები ტესტისთვის:
if __name__ == "__main__":
     print(calculator(10, 5, "+")) # 15
     print(calculator(10, 5, "-")) # 5
     print(calculator(10, 5, "*")) # 50
     print(calculator(10, 5, "/")) # 2.0
     print(calculator(10, 0, "/")) # "cannot divide by zero"
     print(calculator(10, 5, "%")) # Invalid operator


     # drink about
     
     def people_with_age_drink(age):
    #if age < 14:
        return "drink toddy"
    #elif age < 18:
        return "drink coke"
    #elif age < 21:
        return "drink beer"
    #else:
        return "drink whisky"
     
     
     # ტესტები
    # print(people_with_age_drink(10)) # drink toddy
    # print(people_with_age_drink(16)) # drink coke
    # print(people_with_age_drink(18)) # drink beer
    # print(people_with_age_drink(25)) # drink whisky
    

    # century from year
    #def century(year):
    #return(year + 99) // 100

    # ტესტები
    #print(cdntury(1705)) # 18
    #print(century(1900)) # 19
    #print(century(1601)) # 17
    #print(century(2000)) # 20
    #print(century(89)) # 1

    # remove String Spaces
    
    #def no_space(x):
    #return x.replace("","")

    #print(no_space("8 j 8 mBliB8g imjB8B8 jl B")) # "8j8mBliB8gimjB8B8jlB"
    #print(no_space("8 8 Bi fk8h B 8 BB8B B B B888 c hl8 BhB fd")) # "88Bifk8hB8BB8BBBB888chl8BhBfd
    #print(no_space("")) # ""
    #print(no_space("")) # ""
    #print(no_space("    B   ")) #

    
    # how old will I be in 2009
    #def calculate_age(birth, year_to):
    #diff = year_to- birth
   # if diff == 0:
        return "you were born this very year!"
    #elif diff > 0:
        return f"you are {diff} year{'s' if diff != 1 else''} old."
    #else:
        diff = abs(diff)
        return f"you will be born in {diff} year{'s' if diff != 1 else ''}."
     
     # ტესტები
     
     # print(calculate_age(2000,1990) # you will be born in 10 years.
     # print(calculate_age(2000,2000) # you will born this very year!
     # print(calculate_age(2000,2010) # you are 10 years old.
     # print(calculate_age(2000,2001) # you are 1 year old.
     # print(calculate_age(2001,2000) # you will be born in 1 year.



 
