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

```  Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python. As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.``` 

uma diferença entre tuplas e listas são:
Tuplas |  Listas
:---: | ---:  
são imutável|são mutáveis 

Obs: Click [Aqui](https://www.youtube.com/watch?v=N1hTsbW50eM) para acessar essa aula

## Primeiros passos usando lista :
 
### Comando append: 
É usado para adicionar algo a lista

## Ex:
Lanche = ['hamburguer', suco', 'pizza', 'picole']

Lanche.append(' cookie ')

Resultado:

Lanche = ['hamburguer', suco', 'pizza', 'picole', ' cookie ']  
   
# Insert:
 Usamos o comando INSERT quando queremos adicionar um item antes/depois de outro.

## Ex:

   Lanche.insert(0,'Cachorro-Quente')
   
   Obs: Acima estamos indicando a posição que queremos que o "cachorro-quente" fique.
   
### O resultado dessa alteração é

   Lanche = ['Cachorro-Quente', 'hamburguer', suco', 'pizza', 'picole', ' cookie '] 
   
## Comandos para apagar um item da lista:


del Lanche[3]                                     
:---: 
Lanche.pop()
Lanche.remove()   


## Observação:
### Pop:
    Ao utilizarmos o comando Pop, primeiro temos que saber que ele é usado para apagar o ultimo item de uma lista,
    mas podemos apagar qualquer item da lista se passarmos pelo parâmetro
    Exemplo:
    Lanche.pop(3)
    
### Remove:
    Ao utilizarmos o comando Remove, precisaremos passar por parâmetro o nome do item que desejamos excluir
    Exemplo:
    Lanche.remove('Pizza')
   

![Kakashi-Agradecendo-com-o-polegar-em-naruto-removebg-preview](https://user-images.githubusercontent.com/101743377/235382726-75202f70-d29c-4527-b345-aed6ab44de06.png)


