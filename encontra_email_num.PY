import re

# Formato e email e fone base
emailRegex = re.compile(r'([a-zA-Z0-9]+@ [a-zA-Z0-9]+ \.[a-zA-Z]{2,4} )', re.VERBOSE)
phoneRegex = re.compile(r'\(\d\d\) \d\d \d\d\d\d-\d\d\d\d')

# Texto base
texto = 'Meu email é renan2603@gmail.com e meu numero de telefone é (55) 47 9297-4385 meu email é ark.efr@gmail.com e meu numero é (55) 47 9985-5159'

# Verifica texto
a = emailRegex.findall(texto)
b = phoneRegex.findall(texto)
lista_email_num = []


zipper = list(zip(a, b))

# Adiciona e printa os elementos
for i in zipper:
    lista_email_num.append(i)

for i in lista_email_num:
    print(i)
