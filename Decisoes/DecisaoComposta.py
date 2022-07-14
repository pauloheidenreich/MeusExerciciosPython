nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))

if (idade>=65):
    print("O paciente " + nome + " tem " + str(idade) + " e possui prioridade.")

else:
    print("O paciente " + nome + " tem " + str(idade) + " e não possui prioridade.")
