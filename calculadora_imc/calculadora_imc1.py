"""Calculadora de imc #1"""

def obter_dados_usuarios():
    """Essa def coleta os dados da pessoa que vai usar como peso e altura para calcular o imc"""
    while True:
        try:
            peso = float(input("Qual o seu peso: "))
            altura = float(input("Qual a sua altura, em metros: "))
            return peso, altura #aqui vamos retornar o peso e a altura para fora da def
        except ValueError:
            print("tente colocar um numero")

def main():
    """vamos pegar o peso e a altura do obter_dados_usuarios e vamos calcular o imc"""
    peso, altura = obter_dados_usuarios()
    imc = peso / (altura ** 2) #aqui vamos calcular os dados e falar que o imc e o peso/altura²
    print(f"Seu IMC é: {imc:.2f}") #vamos colocar na tela o imc e apenas duas casas depois da virgula

if __name__ == '__main__':
    main()


