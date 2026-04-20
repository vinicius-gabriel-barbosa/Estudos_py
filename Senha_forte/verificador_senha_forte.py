"""Verificador de senha forte"""

#pedir uma senha
def _pedir_senha():
    return input("Digite uma senha: ")

def maiuscula(senha):
    return any(c.isupper() for c in senha)
def minuscula(senha):
    return any(c.islower() for c in senha)
def numero(senha):
    return any(c.isdigit() for c in senha)
def especial(senha):
    especial = "!@#$%^&*()-_=+[]{}|;:,.<>?"
    return any(c in especial for c in senha)
def tamanho(senha):
    return len(senha) >= 8

regras = {
    "letra maiscula": maiuscula,
    "letra minuscula": minuscula,
    "numero": numero,
    "caractere especial": especial,
    "tamanho": tamanho,
}


#verificar se ela e forte ou nao
def verificar_senha(senha):
    #pegar senha verificar o que tem e o que nao tem
    erros = []

    for nome, funcao in regras.items():
        if not funcao(senha):
            erros.append(nome)

    return len(erros) == 0, erros


def main():
    while True:
        senha = _pedir_senha()

        forte, erros = verificar_senha(senha)
        if forte:
            print("senha forte")
            break

        print("senha fraca. problemas encontrados: ")
        for erro in erros:
            print(f" - {erro}")


if __name__ == "__main__":
    main()