num1 = input("Choose a number: ")

num2 = input("Choose another number: ")

thing = input("(A)ddition, (S)ubtraction, (D)ivision or (M)ultiplication: ")

if thing.upper() == "A":
    print(int(num1) + int(num2))
    
elif thing.upper() == "S":
    print(int(num1) - int(num2))

elif thing.upper() == "D":
    print(int(num1) / int(num2))

elif thing.upper() == "M":
    print(int(num1) * int(num2))

input('Press ENTER to exit')