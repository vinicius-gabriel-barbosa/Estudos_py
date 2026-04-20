"""convertor_de_temperaturas"""

#pegar qual e a unidade de medida da temperatura
def _get_unidade_medida():
    print("unidade C = 1")
    print("unidade F = 2")
    print("unidade K = 3")
    while True:
        try:
            unidade = int(input("insira um unidade: "))
            if 1 <= unidade <= 3:
                return unidade
            else:
                print("opicao invalida")
        except ValueError:
            print("tente colocar um numero valido")

#pegar qual a temperatura de acordo com a unidade
def _get_temperatura(unidade):
    while True:
        try:
            if unidade == 1:
                temperatura = float(input("insira um temperatura em C: "))
                return temperatura
            elif unidade == 2:
                temperatura = float(input("insira um temperatura em F: "))
                return temperatura
            elif unidade == 3:
                temperatura = float(input("insira um temperatura em K: "))
                return temperatura
            else:
                print("opicao invalida")
        except ValueError:
            print("tente colocar um numero valido")

#calculos da temperatura
def C(a):
    C1 = (a * 9 / 5) + 32
    C2 = a + 273.15
    return C1, C2
def F(a):
    F1 = (a - 32) * 5 / 9
    F2 = (a - 32) * 5 / 9 + 273.15
    return F1, F2
def K(a):
    K1 = a - 273.15
    K2 = (a - 273.15) * 9 / 5 + 32
    return K1, K2

operacaoes = {
    1:C,
    2:F,
    3:K
}

#fazer os calculos de acorodo com a temperatura
def calculadora(unidade, temperatura):
    opcao =  operacaoes.get(unidade)

    valor1, valor2 = opcao(temperatura)

    unidades_entrada = {1: "°C", 2: "°F", 3: "K"}
    unidades_saida = {
        1: ("°F", "K"),  # Celsius → Fahrenheit, Kelvin
        2: ("°C", "K"),  # Fahrenheit → Celsius, Kelvin
        3: ("°C", "°F")  # Kelvin → Celsius, Fahrenheit
    }

    entrada = unidades_entrada[unidade]
    saida1, saida2 = unidades_saida[unidade]

    output = f"{temperatura:.2f}{entrada} = {valor1:.2f}{saida1} e {valor2:.2f}{saida2}"

    return output

#main
def main():
    unidade = _get_unidade_medida()
    temperatura = _get_temperatura(unidade)
    output = calculadora(unidade, temperatura)
    print(output)


if __name__ == "__main__":
    main()