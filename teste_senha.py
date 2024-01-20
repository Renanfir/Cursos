import re

senha = "aB1234567"

if len(senha) < 8 :
    print('8 caracteres')

if not re.search(r'[A-Z]',senha):
    print('Senha deve ter pelo menos 1 letra maiuscula')

if not re.search(r'[a-z]',senha):
    print('Senha deve ter pelo menos 1 letra minuscula')

if not re.search(r'[0-9]',senha):
    print('Senha deve ter pelo menos 1 numero')

else:
    print('Agora ta show')







