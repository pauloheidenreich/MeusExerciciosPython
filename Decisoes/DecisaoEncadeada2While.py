repeticao="SIM"
while repeticao=="SIM":
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
    while doenca_infectocontagiosa!="SIM" and doenca_infectocontagiosa!="NAO":
        print("Digite Apenas: SIM ou NAO")
        doenca_infectocontagiosa=input("Suspeita de doença infectocontagiosa? ").upper()
    if idade >= 65:
        print("Paciente COM prioridade")
        if doenca_infectocontagiosa == "SIM":
            print("Encaminhe o paciente para sala AMARELA")
        else :
            print("Encaminhe o paciente para sala BRANCA")
    else:
        print("Paciente SEM prioridade")
        if doenca_infectocontagiosa == "SIM":
            print("Encaminhe o paciente para sala AMARELA")
        else :
            print("Encaminhe o paciente para sala BRANCA")
    
    repeticao=input("Você deseja repetir o processo? Digite apenas SIM ou NAO: ").upper()