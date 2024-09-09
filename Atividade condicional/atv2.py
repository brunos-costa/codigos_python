nome = input("Informe seu nome: ")
sexo = input("Informe o sexo - f ou m ")
estadoCivil = input("Qual seu estado civíl: ")

if sexo == "f" and estadoCivil == "casada":
    tempo = int(input("Informe seu tempo de casada: "))
    print(f"Olá {nome}, você tem {tempo} de casada")
else:
    print(f"Olá {nome}, Obrigado e até a próxima")