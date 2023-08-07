cpf = "3655521304" #cpf [e dp tipo str
print("CPF inserido: {}".format(cpf))

if len(cpf) < 11:
    cpf = cpf.zfill(11)
    print("CPF com função zfill(li): {}".format(cpf))

cpf_formatado = "{}.{}.{}-{}".format(cpf[:3], cpf[3:6], cpf[6:9], cpf[9:])
print("CPF formatado: {}".format(cpf_formatado))