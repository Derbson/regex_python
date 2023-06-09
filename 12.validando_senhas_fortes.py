import re

regex = re.compile(r"((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[ -\/:-@['{}^[;_~]).{12,})", flags=re.M)

test_str = ("\n\n"
	"v2Ts7<o9T~}Y\n"
	"j25TTbjJ:6{<\n"
	"s`Mu6T;4M1!y\n"
	"Li`hk6:3WX>3\n"
	"d.D09}^dI2Vn\n\n"
	"I7^Y3RS^ 9]7\n"
	"[P6W\"83L5V{[\n"
	"B7=;K8D6_}W5\n"
	"1B_RT`93R%>1\n"
	"E\n"
	"ZU{7;2&D:64 \n\n"
	"E}LV`C?X_G:{\n"
	"AJH[@HD*V~=<\n"
	"\\A~AC{_V~MG \n"
	"W<-T}W:QAF'{\n"
	"~YJ}|FILN>~)\n\n"
	"PBDZDPECUDNN\n"
	"EJQWFWFFDEHY\n"
	"XRCNLNRHYOZJ\n"
	"TWIYPLWUDMNN\n"
	"JMDTJSEPKVON\n\n"
	"Iu4<1j\n"
	"1x`P6g\n"
	"@9t3Ry\n"
	"qf9_6H\n"
	"0o`9fO\n\n")

print(regex.findall(test_str))
