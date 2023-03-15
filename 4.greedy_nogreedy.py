# meta caracteres: ^ $ ( )

# * 0 ou n
# + 0 ou n
# ? 0 ou 1

import re

texto = '''
<p>Frase 1</p> <p>qualquer frase</p> <p>terceira frase de teste</p> <div>Frase 4</div> 
'''

# greedy
# print(re.findall(r'<[dpiv]{1,3}>.*<\/[dpiv]{1,3}>', texto))

# no greedy
print()
print(re.findall(r'<[dpiv]{1,3}>.*?<\/[dpiv]{1,3}>', texto))


 