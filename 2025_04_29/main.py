from re import search, match, findall
from colorama import Fore

class Regex:
    
    def enum(string : str) -> bool:
        pattern = r"^\d+$"
        if match(pattern, string): return True
        else: return False
        
    def teste(string: str) -> str:
        pattern = r"^...$"
        res = search(pattern, string)
        if res is not None: return res.group()
        else: return 'Quebrou nosso esquema :('
        
    def valida_email(string: str) -> bool:
        pattern = r"^[\w\.-]+@[\w\.]+\w$"
        if match(pattern, string): return True
        else: return False
    
try:
    '''
    while True: 
        i = input('Digite algo:\n> ')
        print(Regex.teste(i))
    '''
    while True:
        i = input('Digite algo:\n> ')
        if Regex.valida_email(i):
            print('OK')
        else:
            print('Azedou')
        
except KeyboardInterrupt: print('<end>')