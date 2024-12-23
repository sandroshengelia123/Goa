password = 12345678910

while True:
    enter_password = int(input("Enter the password"))
    while enter_password != password:
        enter_password = int(input("the password is wrong! try again:"))
    print("you have entered your account")