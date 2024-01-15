import re

lista = ["Olá Renan","Bom dia Renan","Boa Tarde Renan","a","b","","c","d","Renan","ABCD","PQRS","Renan"]

def achador_texto(elemento):
    base = re.compile(r'Renan') 
    retorno = base.findall(elemento)
    print(retorno)

for i in lista:
    achador_texto(i)





