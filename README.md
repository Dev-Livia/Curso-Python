### Lista de tarefas:
- [x] Mundo 1
- [x] Mundo 2  
- [ Em Andamento ] Mundo 3
- Obs: Talvez esteja faltando alguns exercicíos, pois foram perdidos antes que eu 
adquire-se conhecimento em git e github,
mas aos poucos farei com que tudo isso fique em ordem com todos os conteúdos :)


# Este é o README do curso Python 3 
   Olá, este repositório contém exercícios propostos pelo professor Gustavo Guanabara, através da plataforma Curso em Vídeo 
também disponível no YouTube

# Mundo 1 
*EM BREVE*

# Mundo 2
*EM BREVE*

# Mundo 3 
## Aula 16 - Tuplas 
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python. As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

## Exemplo de como usamos as tuplas:
```
lanche = 'hambúrger', 'Suco', 'Pizza', 'Picolé'
'''print(lanche[1]) 
print(lanche[-2])
print(lanche[1:3])'''

print('=' * 30)

# Vocês sabiam que tuplas são imutáveis ?

#Exemplo
'''lanche[1] = Refrigerante'''

# logo o código dara erro pois enquanto o programa está funcionando é impossivel alterar algum valor

'''Usando o for 
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Hmm estava uma delícia')'''

# resultado  : 

Eu vou comer hambúrger
Eu vou comer Suco
Eu vou comer Pizza
Eu vou comer Picolé
Hmm estava uma delícia
```
# Aula 17
## Listas:

Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.

uma diferença entre tuplas e listas são:
Tuplas |  Listas
:---: | ---:  
são imutável|são mutáveis

Obs: Click [Aqui](https://www.youtube.com/watch?v=N1hTsbW50eM) para acessar essa aula

### Primeiros passos usando lista :
`` 
#### Comando append:
   É usado para adicionar algo a lista
   
   Lanche = ['hamburguer', suco', 'pizza', 'picole']
   
#### Ao usarmos "Append" a nossa Lista será alterada e o  item "cookie"
 passará a existir na lista
 
#### Ex:
   Lanche.append(' cookie ')
   Lanche = ['hamburguer', suco', 'pizza', 'picole', ' cookie ']
   
#### Insert:
Usamos o comando INSERT quando queremos adicionar um item antes/depois de outro.

Ex:
   Lanche.insert(0,'Cachorro-Quente')
   
#E o resultado dessa alteração é

   Lanche = ['Cachorro-Quente', 'hamburguer', suco', 'pizza', 'picole', ' cookie ']

#### Comandos para apagar um item da lista:
Podemos usar:

del lanche(3)
   ou
lanche.pop()

##Observação:
    o comando "pop" geralmente é utilizado para deletar o útimo item da lista, 
    mas podemos deletar o item que quisermos se passarmos pelo parametro, como no exemplo a baixo 
   
   
  ![imagem_2023-04-29_231734085](https://user-images.githubusercontent.com/101743377/235332408-2bdd6d49-9aae-4186-abeb-b70f4b1cdef6.png)
   
   lanche.pop(3)
``




