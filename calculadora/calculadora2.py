# calculadora

def _num_ ():
    num1 = float(input("digit one number: "))
    num2 = float(input("digit two number: "))
    return num1, num2

def _option_ ( ):
    print("Oprion:\n 1 = +\n 2 = -\n 3 = * \n 4 = / \n 5 = %")
    option = int(input("digit option: "))
    return option

def _cal_ (num1, num2, option):
    if option == 1:
        print(num1 + num2)
    elif option == 2:
        print(num1 - num2)
    elif option == 3:
        print(num1 * num2)
    elif option == 4:
        print(num1 / num2)
    elif option == 5:
        res = num1 % num2
        if res % 2 == 0:
            print("{sla} is even")
        else:
            print("{sla} is odd")

def main():
    num1, num2 = _num_()
    option = _option_()
    _cal_(num1, num2, option)

if __name__ == "__main__":
    main()