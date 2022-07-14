nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
prioridade = "Não"

if idade>= 65:
    prioridade = "SIM"

print ("O paciente " + nome + " possui " + str(idade) + " anos de idade. Ele possui prioridade ? " + prioridade)