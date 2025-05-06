from re import match, findall

class Login:pass

class CPF:

    def __init__(self, cpf : str) -> None:
        self.cpf = self.formataCPF(cpf)
        
    def formataCPF(self, cpf: str) -> str | None:
        
        # Criação dos objetos a serem validados
        numeros : list[str] = findall(r"\d", cpf)
        numeros_int : list[int] = [int(x) for x in numeros]
        
        # Chamada das funções de validação
        if not self.verificaCPF(numeros): return None
        if not self.validaCPf(numeros_int): return None
        return "".join(numeros)
            
    def verificaCPF(self, cpf : list) -> bool:
        if len(cpf) != 11: return False
        return True
    
    def validaCPf(self, numeros_cpf : list) -> bool:
        # Tratando números do CPF
        cpf_base = numeros_cpf[0:9]
        validador1 = numeros_cpf[9]
        validador2 = numeros_cpf[10]
        
        # Primeira Validação
        multiplicador = 10
        soma_cpf = 0
        for n in cpf_base:
            soma_cpf += n * multiplicador
            multiplicador -= 1
            
        validator = soma_cpf % 11
        
        if validator < 2: digito = 0
        else: digito = 11 - validator
        
        if digito != validador1: return False
        
        # Segunda Validação
        multiplicador = 11
        soma_cpf = 0
        cpf_validador = cpf_base
        cpf_validador.append(validador1)
        
        for n in cpf_validador:
            soma_cpf += n * multiplicador
            multiplicador -= 1
            
        validator = soma_cpf % 11
        
        if validator < 2: digito = 0
        else: digito = 11 - validator
        
        if digito != validador2: return False
        
        return True