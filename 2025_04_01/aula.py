from sys import argv as argumentos

class Calc:
    def __init__(self, n1, op, n2):
        self.operadores = {"+":(Calc.soma,"soma"), "-":(Calc.sub,"Subtração"), "*":(Calc.mult,"Multiplicação"), "/":(Calc.div,"Divisão")}
        self.n1 = float(n1)
        self.n2 = float(n2)
        self.op = op
        print(f"O resultado da {self.operadores[op][1]} de {n1} e {n2} é: {self.operadores[op][0](self)}")
        
    def soma(self): return self.n1 + self.n2
    def sub(self): return self.n1 - self.n2
    def mult(self): return self.n1 * self.n2
    def div(self): return self.n1 / self.n2

class main():
    argumentos.pop(0)
    try:
        if len(argumentos) !=3: 
                raise Exception
        n1,op,n2 = argumentos
        calculadora = Calc(n1,op,n2)
    except:
        print("Comando usado incorretamente")
        print("\tUsage: python .\aula.py num1 operator num2")
        print("\t\tEx: aula.py 10 + 5")
    

if __name__ == '__main__': main()
