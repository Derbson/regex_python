# meta caracteres ^ $
# ^ --> começa com
# $ --> terman com
# ^ dentro de um conjunto é negação do conjunto
#ex: [^a-z] == não pode ter valores entre a-z

import re


cpf = '123.456.789-45'

print(re.findall(r'^((?:[0-9]{3}\.){2}[0-9]{3}\-[0-9]{2})$', cpf))
print(re.findall(r'[^0-9]+', cpf))

