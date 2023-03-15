import re
from pprint import pprint


test_str = ("(85) 9 9945-4567\n"
	"(85)94455-7788\n"
	"(11)      9955-1231\n"
	"(35)  9  9975-4521\n"
	"(31) 3851-2587\n"
	"9 8571-5213\n"
	"1234-5678\n")

""" ------------------- valida todos ------------------------------ """
todos = re.compile(r"((?:\(\d{2}\)\s*)?(?:9\s*)?(?:\d{4})\-\d{4})", flags=re.M)


""" ------------------- (ddd) 9 1234-1234 --------------------------- """
padrao_br = re.compile(r"(^(?:\(\d{2}\)\s)(?:9\s)(?:\d{4})\-\d{4}$)", flags=re.M)


# pprint(todos.findall(test_str))

# pprint(padrao_br.findall(test_str))

for telefone in todos.findall(test_str):
    print(telefone)
