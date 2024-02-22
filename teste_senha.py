import re

senha = "aB1234567"




# Verifica se a senha é maior do que 8 digitos,
if len(senha) < 8:
    print('8 caracteres')

# se contem uma letra maiuscula
if not re.search(r'[A-Z]', senha):
    print('Senha deve ter pelo menos 1 letra maiuscula')


# se contem uma letra minuscula
if not re.search(r'[a-z]', senha):
    print('Senha deve ter pelo menos 1 letra minuscula')


# se contem um numero
if not re.search(r'[0-9]', senha):
    print('Senha deve ter pelo menos 1 numero')

else:
    print('Agora ta show')







