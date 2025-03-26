def even_number(n):
    return[i for i in range(1, n + 1) if i % 2 == 0]

# მომხმარებლისგან რიცხვის შემოტანა
num = int(input("შეიყვანეთ"))


# ფუნქციის გამოძახება და შედეგის დაბეჭდვა
print(even_number(num))