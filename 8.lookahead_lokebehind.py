""" --------------- lookeahead e lookbehind ------------------------- """

import re
from pprint import pprint

texto = '''
ONLINE 192.168.0.1 GHIJK active
OFFLINE 192.168.0.2 GHIJK inactive
OFFLINE 192.168.0.3 GHIJK active
ONLINE 192.168.0.4 GHIJK active
ONLINE 192.168.0.5 GHIJK active
ONLINE 192.168.0.6 GHIJK inactive
OFFLINE 192.168.0.7 GHIJK active
'''

""" ---------------------------- lookahead -------------------------------- """

# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(\w+)', texto))
# print()
# prositive lookahead
# print('active')
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?=active)', texto))
# pprint(re.findall(r'(?=.*[^in]active).+', texto))

# negative lookahead
# print('negative')
# pprint(re.findall(r'\w+\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+(?!active)', texto))
# pprint(re.findall(r'(?!.*[^in]active).+', texto))


""" --------------------------- lookbehind -------------------------------- """

# pprint(re.findall(r'(\w+)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# print()

""" ----------------------- positive lookbehind --------------------------- """

# print('ONLINE')
# pprint(re.findall(r'\w+(?<=ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# print('OFFLINE')
# pprint(re.findall(r'\w+(?<=OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))

""" ----------------------- negative lookbehind ---------------------------- """

# print('ONLINE')
# pprint(re.findall(r'\w+(?<!OFFLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))
# print('OFFLINE')
# pprint(re.findall(r'\w+(?<!ONLINE)\s+(\d+\.\d+\.\d+\.\d+)\s+\w+\s+\w+', texto))


