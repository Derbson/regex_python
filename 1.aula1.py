import re

# findall: encontra todas as ocorrências da expressão 
# 
# search: encontra uma ocorrência da expressão e retonar um objeto match
# sub: substitui todas as ocorrências de uma determinada expressão
# compile: compila expressões regulares


string = 'Este é um teste de expressões teste regulares.'

print(re.search(r'teste', string))
print(re.findall(r'teste', string))
# substituir um valor 
print(re.sub(r'teste', 'ABC', string, count=1))

regexp = re.compile(r'teste')
print(regexp.search(string))
print(regexp.findall(string))
print(regexp.sub('ABC',string))
