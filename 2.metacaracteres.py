# meta caracteres: . ^ $ + ? { } [ ] \ | ( )

# | OU
# . Qualquer caractere (com exceção de quebra de linha)
# [] conjunto de caracteres

import re


texto = '''
    João trouxe flores para sua namorada em 10 de janeiro de 1970,
    Maria era o nome dela.
    
    Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
    maria, hoje sua esposa, ainda faz aquele café com pão de quijo nas tardes de 
    domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
    pão de queijo.
    Não canso de ouvir a Maria:
    "Jooooooooooãaaaoo, o café ta pronto aqui, veeem!!"
'''

# print(re.findall(r'João|Maria|ad....s', texto))

# print(re.findall(r'[Jj]oão|[Mm]aria', texto))

# print(re.findall(r'[a-zA-Z]aria', texto))

print(re.findall(r'jOãO|mArIa', texto, flags=re.I))
