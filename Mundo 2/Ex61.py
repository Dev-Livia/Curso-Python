#Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1

print("Os 10 primeiros termos da PA são:")

while contador <= 10:
    print(termo_atual, end=" ")
    termo_atual += razao
    contador += 1

print()  # Pula uma linha após exibir os termos
