##calculadora

number__1 = float(input("digit one number: "))
number__2 = float(input("digit two number: "))

print(number__1, number__2)

print("options, \n 1 = + \n 2 = - \n 3 = * \n 4 = / \n 5 = %")

option = int(input("choose option: "))

if option == "1":
    print("your option is, {option}")
    print(number__1 + number__2)

elif option == "2":
    print("your option is, {option}")
    print(number__1 - number__2)

elif option == "3":
    print("your option is, {option}")
    print(number__1 * number__2)

elif option == "4":
    print("your option is, {option}")
    print(number__1 / number__2)

elif option == "5":
    print("your option is, {option}")
    print(number__1 % number__2)

else:
    print("invalid option")