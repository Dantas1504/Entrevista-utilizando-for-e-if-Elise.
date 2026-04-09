print("Bem-vindo a TudoWeb, gostaríamos de saber a sua opinião sobre nossos serviços.")

qtd_excelente = 0
qtd_ruim = 0

for i in range(50):
    print("Entrevistado", i+1)

    nome = input("Qual é o seu nome? ")
    idade = int(input("Qual é a sua idade? "))
    opiniao = input("Qual é a sua opinião sobre o atendimento prestado? (1 - Excelente, 2 - Bom, 3 - Ruim): ")

    if opiniao == "1":
        qtd_excelente += 1
    elif opiniao == "3":
        qtd_ruim += 1

# Resultado final
print("RESULTADO DA PESQUISA:")
print(f"Excelente: {qtd_excelente}")
print(f"Ruim: {qtd_ruim}")