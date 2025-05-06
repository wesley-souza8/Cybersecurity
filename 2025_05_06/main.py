from scripts.login import CPF

if __name__ == '__main__':
    cpf = CPF(input("Digite um CPF:\n> "))
    print(cpf.cpf)
    