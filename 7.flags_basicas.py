
# \w == [a-zA-Z0-9À-ú_]
# \W == [^a-zA-Z0-9À-ú_]
# \d == [0-9]
# \D == [^0-9]
# \s == [ \r\n\f\t]
# \S == [^ \r\n\f\t]
# \b 
#
# re.A --> ASCII
# re.I --> IGNORECASE
# re.M --> Multiline
# re.S --> Dotall


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

#print(re.findall(r'\w+', texto, flags=re.I))
#print(re.findall(r'\D+', texto, flags=re.I))
#print(re.findall(r'\d+', texto, flags=re.I))

#print(re.findall(r'\b\w+neiro', texto, flags=re.I))
#print(re.findall(r'\b\w{4}\b', texto, flags=re.I))

""" ----------------------- re.M --> Multiline ----------------------- """
cpf_lines = '''
131.768.406-53 ABC
055.123.060-50 DEF
955.651.060-90
'''
# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf_lines, flags=re.M))
# print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', cpf_lines, flags=re.M))
# print(re.findall(r'^\d{3}\.\d{3}\.\d{3}\-\d{2}$', cpf_lines))
# print(re.findall(r'\d{3}\.\d{3}\.\d{3}\-\d{2}', cpf_lines))

""" ------------------------ re.S --> Dotall --------------------------- """

texto2 = '''
O joão gosta de folia   
e adora ser amado
'''

print(re.findall(r'^o.*o$', texto2, flags=re.I))
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S))
print(re.findall(r'^o.*o$', texto2, flags=re.I | re.S |re.M))



