"""primeria calculadora"""

def get_number_ ():
    """pegar os dois numeros"""
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))
    return num1, num2

def option_ ():
    """pegar opicao"""
    print("opicoes")
    print("option 1 = +")
    print("option 2 = -")
    print("option 3 = *")
    print("option 4 = /")
    while True:
        try:
            oprion = int(input("escolha a opicao (1-4): "))
            if 1<=oprion<=4:
                return oprion
            else:
                print("opicao invalida")
        except ValueError:
            print("tente colocar um numero")

def add (a, b):
    return a + b, None

def sub (a, b):
    return a - b, None

def mul (a, b):
    return a * b, None

def div (a, b):
    if b == 0:
        return None, "divisao invalida"
    return a / b, None

operadores = {
    1:add,
    2:sub,
    3:mul,
    4:div
}

def calculadora (num1, num2, option):
    """executa o calculo"""
    operacao = operadores.get(option)

    if operacao == None:
        return "operacao invalida"

    result, extra = operacao(num1, num2)

    if result is None:
        return f"erro: {extra}"

    output = f"resultado: {result}"

    return output

def main():
    numero1, numero2 = get_number_()
    option = option_()
    result = calculadora(numero1, numero2, option)
    print(result)

if __name__ == "__main__":
    main()
