# meta caracteres: ^ $ + ? { } ( )

# * 0 ou n
# + 0 ou n
# ? 0 ou 1
# {n}
# {1,} 1 ou mais vezes
# {,10} até 10 vezes
# {10} exatamente 10 vezes
# {5,10} de 5 a 10
# {min, max}

import re

texto = '''
    João trouxe flores para sua namorada em 10 de janeiro de 1970,
    Maria era o nome dela.
    
    Foi um ano excelente na vida de joão. Teve 5 filhos, todos adultos atualmente.
    maria, hoje sua esposa, ainda faz aquele café com pão de quijo nas tardes de 
    domingo. Também né! Sendo a boa mineira que é, nunca esquece seu famoso
    pão de queijo.
    Não canso de ouvir a Maria:
    "Jooooooooooããããoo, o café ta pronto aqui, veeeem!!"
'''

#print(re.findall(r'jo+ã+o+', texto, flags=re.I))
#print(re.findall(r've+m', texto, flags=re.I))
#print(re.findall(r've{1,}m', texto, flags=re.I))
#print(re.findall(r'n[a-z]{4}', texto, flags=re.I))
#print(re.findall(r'n[a-z]*', texto, flags=re.I))
#print(re.sub(r'jo+ã+o+','Felipe', texto, flags=re.I))

