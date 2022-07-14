nivelAcesso = input("Digite o seu nível de acesso (ADM, USR ou GUEST): ").upper()
if nivelAcesso == "ADM" or nivelAcesso == "USR":
    genero = input("Qual é o seu gênero (MASCULINO, FEMININO) ? ").upper()
    if nivelAcesso == "ADM":
        if genero == "FEMININO":
            print("Olá Administradora.")
        else:
            print("Olá Administrador.")
    else:
        if nivelAcesso == "USR":
            if genero == "FEMININO":
                print("Olá usuária.")
            else:
                print("Olá usuário.")
elif nivelAcesso == "GUEST":
    print("Olá Convidado.")
else:
    print("Olá desconhecido.")