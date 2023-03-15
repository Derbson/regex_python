import re
from pprint import pprint

regex = re.compile(r"^(?!(\d)\1{2}\.\1{3}\.\1{3}\-\1{2})(\d{3}\.\d{3}\.\d{3}\-\d{2})$", flags=re.M)

test_str = ("689.547.528-54\n"
	"994.083.055-66\n"
	"738.109.391-02\n"
	"128.459.762-83\n"
	"873.128.461-22\n"
	"761.325.812-27\n"
	"255.076.412-93\n"
	"738.646.233-67\n"
	"417.914.778-52\n"
	"000.000.000-01\n"
	"000.000.000-00\n"
	"111.111.111-11\n"
	"222.222.222-22\n"
	"333.333.333-33\n"
	"444.444.444-44\n"
	"555.555.555-55\n"
	"666.666.666-66\n")

pprint(regex.findall(test_str))
