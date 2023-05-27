#Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))

termo_atual = primeiro_termo
contador = 1
mais_termos = True

print("Os termos da PA são:")

while mais_termos:
    print(termo_atual, end=" ")
    termo_atual += razao
    contador += 1

    if contador > 10:
        opcao = int(input("\nDeseja mostrar mais alguns termos? Digite a quantidade desejada (0 para encerrar): "))
        if opcao == 0:
            mais_termos = False
        else:
            contador = 1

print("Programa encerrado.")
