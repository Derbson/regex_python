
# ()        \1
# () ()     \2
# (())()    \3
# os grupos são númerados na ordem que é aberto parentese ( () )
#                                                         \1 \2
# ?: para não salvar um grupo

import re

texto = '''
<p>Frase 1</p> <p>qualquer frase</p> <p>terceira frase de teste</p> <div>Frase 4</div>
'''


""" ------------------------- grupo e retrovisores ------------------------ """

#tags = re.findall(r'(<([dpiv]{1,3})>(.*?)<\/\2>)', texto)
#for tag in tags:
#    um, dois, tres = tag
#    print(tres)

#print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1\3\4', texto))

conteudo = re.findall(r'(<(.+?)>)(.+?)(<\/\2>)', texto)

for tag in conteudo:
   print(tag[2])

#cpf = '123.456.789-23'

#print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})', cpf))



 