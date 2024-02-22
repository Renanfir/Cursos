import re

# Lista de testes
lista = ["Olá Renan", "Bom dia Renan", "Boa Tarde Renan", "a", "b", "", "c", "d", "Renan", "ABCD", "PQRS", "Renan"]

# Verifica se cada frase tem a palavra Renan
def achador_texto(elemento):
    base = re.compile(r'Renan') 
    retorno = base.findall(elemento)
    print(retorno)

# Printa os resultados encontrados
for i in lista:
    achador_texto(i)





