"""Conversor de temperatura"""

unidade_entrada = {1: "°C", 2: "°F", 3: "K"} # marca qual vai ser a unidade dos valores mais a frente
unidade_saida = {
    1: ("°F", "K"),  # Celsius → Fahrenheit, Kelvin
    2: ("°C", "K"),  # Fahrenheit → Celsius, Kelvin
    3: ("°C", "°F")  # Kelvin → Celsius, Fahrenheit
}

def obter_unidade(): # faz a pergunta de qual vai ser a unidade recebida
    """perguntar qual a unidade de temperatura"""
    print("escolha a unidade da tempratura")
    print("  1 - Celsius (°C)")
    print("  2 - Fahrenheit (°F)")
    print("  3 - Kelvin (K)")

    while True:
        try: # verifica se o valor recebido e correto
            unidade = int(input("insira uma unidade de temperatura: "))
            if 1 <= unidade <= 3:
                return unidade
            print("opicao invalida, tente 1, 2 ou 3") # serve como um else mas sem chamar a funcao
        except ValueError: # caso a pessoa digitar algo que nao seja um numero
            print("opicao invalida, tente um numero de 1 a 3")

def obter_temperatura(unidade): # pega a unidade corespondente e pergunta com a temperatura
    """pergunta e valida qual a temperatura"""
    temperatura = unidade_entrada[unidade] #puxa a unidade de entrada la de cima para fazer a verificacao

    while True:
        try: # pergunta qual e a temperatura
            return float(input(f"digite a temperatura em {temperatura}"))
        except ValueError:
            print("opicao invalida, tente um numero")

def converter_de_celsius(c): # converte celsius para as outras temperaturas
    F = (c * 9 / 5) + 32
    K = c + 273.15
    return F, K

def converter_de_fahrenheit(f): # converte fahrenheit para as outras temperaturas
    C = (f - 32) * 5 / 9
    k = (f - 32) * 5 / 9 + 273.15
    return C, k

def converter_de_kelvin(k): # converte kelvin para as outras temperaturas
    C = k - 273.15
    F = (k - 273.15) * 9 / 5 + 32
    return C, F

operacoes = { # mostra de acordo com os valores qual vai ser o calculo
    1: converter_de_celsius,
    2: converter_de_fahrenheit,
    3: converter_de_kelvin
}

def calcular_conversao (unidade, temperatura): # faz o calculo com a unidade
    funcao_converter = operacoes[unidade]
    valor1, valor2 = funcao_converter(temperatura) # tira da tupla o valor 1 e o valor 2 do calculo

    entrada = unidade_entrada[unidade]
    saida1, saida2 = unidade_saida[unidade] # tira da tupla a saida 1 e a saida 2 da unidade saida

    return (
        f"{temperatura:.2f}{entrada} = {valor1:.2f}{saida1}\n" # printa as duas unidades
        f"{temperatura:.2f}{entrada} = {valor2:.2f}{saida2}"
    )

def main():
    unidade = obter_unidade() # trasforma o obter unidade na propria unidade
    temperatura = obter_temperatura(unidade) # trasforma o obter temperatura na propria temperatura

    resultado = calcular_conversao(unidade, temperatura) # faz o calculo de acordo com a unidade e a temperatura
    print(f"\n{resultado}") # printa o resultado

if __name__ == "__main__":
    main()