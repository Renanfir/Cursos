# Função com critérios do formato de numero de telefone
def e_numero_celular(text):
    
    if len(text) != 12: 
        return False
    
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
        
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
        
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-':
        return False
    
    return True


mensagem = 'Me ligue em 415-555-1011 amanhã. 415-555-9999 é do meu escritorio'

# Verificador
for i in range(len(mensagem)):
    pedaco = mensagem[i:i+12]
    if e_numero_celular(pedaco):
        print('Numero de telefone encontrado', pedaco)

print('feito')
