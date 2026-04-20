"""Verificador de senha forte"""

def _pedir_senha(): # vai pedir a senha para o usuario
    return input("Digite sua senha: ")


def maiuscula(senha): # faz a verificacao se tem maiuscula
    return any(c.isupper() for c in senha)


def minuscula(senha): # faz a verificacao se tem minuscula
    return any(c.islower() for c in senha)


def numero(senha): # faz a verificacao se tem numero
    return any(c.isdigit() for c in senha)


def especial(senha): # faz a verificacao se tem caracter especial
    especiais = "!@#$%^&*()-_=+[]{}|;:,.<>?" # fala quais sao os caracters especiais
    return any(c in especiais for c in senha)


def tamanho(senha): # faz a verificacao do tamanho
    return len(senha) >= 8

regras = { # define o nome do erro e a funcao de teste
    "Minimo 8 caracteres": tamanho,
    "Falta letra maiuscula": maiuscula,
    "Falta letra minuscula": minuscula,
    "Falta numero": numero,
    "Falta caracter especial": especial
}


def verificar_senha(senha): # verifica se regra falhou ou se esta correta
    erros = []
    for nome, funcao in regras.items():
        if not funcao(senha): # verifica se nao tem a funcao na senha caso nao adiciona para a lista o nome do erro
            erros.append(nome)
    return len(erros) == 0, erros # retorna (True/False, lista): True se len=0 (forte), False se tem erros; + a própria lista de erros


def main():
    while True: # faz um loop ate a senha ser forte
        senha = _pedir_senha() # chama a função e guarda o valor retornado na variável 'senha'
        forte, erros = verificar_senha(senha) # tira da tupla o len(erros) == 0 e o erros

        if forte: # caso for forte com o break termina o loop
            print("Forte")
            break

        print("\nSenha Fraca. Problemas encontrado: ")
        for erro in erros: # caso for fraca o loop continua
            print(f" - {erro}") # vai mostrar quais sao os erros


if __name__ == "__main__":
    main()