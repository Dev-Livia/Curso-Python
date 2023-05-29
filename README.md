# Este é o README do curso Python 3 
   Olá, este repositório contém exercícios propostos pelo professor Gustavo Guanabara, através da plataforma Curso em Vídeo 
também disponível no YouTube

### - Lista de tarefas:
- [x] Mundo 1
- [x] Mundo 2  
- [ Em Andamento ] Mundo 3
- Obs: Talvez esteja faltando alguns exercicíos, pois foram perdidos antes que eu 
adquire-se conhecimento em git e github,
mas aos poucos farei com que tudo isso fique em ordem com todos os conteúdos :)

# - Mundo 1 
### - Primeiros comandos 
```
Vamos realizar nosso primeiro comando em python, nesse comando vamos imprimir uma mensagem:
podemos usar:

print('Olá, Mundo!!')

ou podemos armazenar o texto em uma variável e imprimir como no exemplo a baixo:

msg = 'Olá, Mundo'
print(msg)

Resultado:
Olá, Mundo
```

### - Aula 06 - Tipos Primitivos e Saída de Dados
```
Nessa aula, vamos aprender como funcionam os tipos primitivos no Python e as peculiaridades do int() float() bool() e str().
Além disso, veremos como fazer as primeiras operações com a função print() do Python.

# int:
é responsável por armazenar números inteiros.
Ex: 1, 2, 3... -1, 0

# Float:
é responsavel por armazenar números reais.
Ex: 4.5, 0.075, -15.223

# Bool:
é responsável por aceitar apenas dois tipos de números
Ex: True or False

# Str
Aceita quelquer tipo de dado:
Ex: 'Olá', 20, 7.0
```
### - Indentificando os tipos primitivos :

type | Vai analisar e retornar o tipo que foi digitado 
:---: | ---: 
isspace | Vai indentificar se possui apenas espaços  
isnumeric | Vai indentificar se os valores são apenas números
isalpha | Vai analisar se os valores são apenas alfabéticos
isalnum | Vai analisar se os valores digitados são apenas números
isupper | Essa função indentifica se os valores digitados então em letras maiúsculas
islower | Essa função indentifica se os valores digitados estão em letras minúsculas
istitle | Essa função vai analisar se existe nas palavras letras minúsculas e maiúsculas

### - Exemplo: 

```
al = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(al))
print('Só tem espaços? ', al.isspace())
print('é um número? ', al.isnumeric())
print('é alfabético? ', al.isalpha())
print('É alfanumérico? ', al.isalnum())
print('Está em maiúsculas? ', al.isupper())
print('Está em mínusculas?', al.islower())
print('Está captalizada? ', al.istitle())

RESULTADO

Digite algo: Python
O tipo primitivo desse valor é  <class 'str'>
Só tem espaços?  False
é um número?  False
é alfabético?  True
É alfanumérico?  True
Está em maiúsculas?  False
Está em mínusculas? False
Está captalizada?  True

```


### - Aula 7 
Nessa aula, vamos aprender quais são os operadores aritméticos do Python e também sua ordem de precedência dentro de expressões matemáticas. 
Veja como funcionam os operadores de adição, subtração, multiplicação, divisão, exponenciação e quociente na linguagem Python.

## - Operações Aritméticas :

' + '| Adição
:---: | ---: 
' - '| Subtração
' * '| Multiplicação
' / '| Divisão
' ** ' | Potência
' // '| Divisão Inteira
' % '| Resto da Divisão

## - Ordem de Precedência
1 | ( )
:---: | ---: 
2 | **
3 | *, /, //, %
4 | +, -

### - Aula 08 - Utilizando Módulos
Nessa aula, vamos aprender como utilizar módulos em Python utilizando os comandos import e from/import no Python.
Veja como carregar bibliotecas de funções e utilizar vários recursos adicionais nos seus programas utilizando módulos built-in e módulos externos, oferecidos no Pypi.

## - Comando para fazer importações de Módulos

Import Random | Ao execultar esse código ele vai importar tudo o que existe dentro do modulo de Random
:---: | ---: 
From Random Import randint| Ao execultar este código, Voçê importará apenas o item escolhido 

# - Vamos aprender um pouco sobre algumas funcionalidades dos módulos?
## - Módulo math
ceil | faz arredondamento para cima 
:---: | ---: 
floor | faz arredondamento para baixo
trunc | elimina números
pow | é utilizado para fazer calculos de potência
sqrt | Calcula raiz Quadrada
factorial | Faz calculo factorial

### - Exemplo a baixo 
   ↓↓↓
``` 
import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é igual a {}'.format(num, math.ceil(raiz)))
```

### - Aula 9
Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String,
Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

len()| retorna o comprimento de uma sequência, como uma string, lista ou tupla.
:---: | ---: 
count() | retorna o número de ocorrências de um determinado elemento em uma sequência.
find() | retorna o índice da primeira ocorrência de uma substring em uma string. Retorna -1 se a substring não for encontrada.
replace() | substitui todas as ocorrências de uma substring por outra substring em uma string.
upper() | converte todos os caracteres de uma string para letras maiúsculas.
lower() | converte todos os caracteres de uma string para letras minúsculas.
capitalize() | converte o primeiro caractere de uma string para maiúscula e os demais para minúsculas.
title() | converte a primeira letra de cada palavra em uma string para maiúscula e o restante para minúsculas.
strip() | remove espaços em branco no início e no final de uma string.
join() | junta os elementos de uma sequência em uma única string, usando um separador especificado.


### - Aula 10 - if... else
O if...else é uma estrutura de controle utilizada em programação para tomar decisões com base em uma condição.
Ela permite que o programa execute diferentes blocos de código dependendo se uma determinada condição é verdadeira ou falsa.

Simplificando, o if verifica se uma condição é verdadeira. Se a condição for verdadeira, o bloco de código dentro do if é executado. Caso contrário,
o programa pode executar um bloco de código alternativo dentro do else.

```
idade = 18

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

Neste exemplo, o programa verifica se a variável idade é maior ou igual a 18. Se for, ele imprime a mensagem "Você é maior de idade". Caso contrário, ou seja, se a condição for falsa, ele imprime a mensagem "Você é menor de idade".

O if...else permite que você tome diferentes caminhos de execução com base em condições, o que é útil para lidar com situações em que o comportamento do programa precisa variar dependendo dos valores das variáveis ou de outros fatores.




# Mundo 2
### - Aula 12 - Condições Aninhadas

Condições aninhadas são estruturas de decisão que permitem que um bloco de código condicional seja colocado dentro de outro bloco de código condicional. Essa aninhamento permite uma lógica mais complexa e granular em seu programa. 

```
x = 10

if x > 0:
    if x > 5:
        print("x é maior que 5")
    else:
        print("x é menor ou igual a 5")
else:
    print("x é igual a 0 ou menor")


```
Neste exemplo, temos uma estrutura de decisão aninhada. Primeiro, verificamos se x é maior que zero. Se for, entramos no bloco de código interno e verificamos se x é maior que 5. Se essa condição for verdadeira, a mensagem "x é maior que 5" será impressa. Caso contrário, se x for menor ou igual a 5, a mensagem "x é menor ou igual a 5" será impressa. Por fim, se x for igual a zero ou menor, a mensagem "x é igual a 0 ou menor" será impressa.

No exemplo acima, se x tiver o valor 10, a saída será:

```
x é maior que 5
```

As condições aninhadas permitem que você lide com lógicas mais complexas, onde você precisa considerar múltiplas condições em diferentes níveis de aninhamento. No entanto, tenha cuidado para manter o código legível e evitar aninhamentos excessivos, pois isso pode tornar o código mais difícil de entender e dar manutenção.

### - Aula 13 - Estrutura de repetição for
A estrutura de repetição for em Python é usada para iterar sobre uma sequência (como uma lista, uma string, um dicionário, etc.) ou outro objeto iterável. Ela permite executar um bloco de código para cada elemento na sequência, até que todos os elementos tenham sido percorridos.

A sintaxe básica do loop for é a seguinte:
```
for elemento in sequência:
    # Código a ser executado para cada elemento

```
O bloco de código dentro do for será executado para cada elemento na sequência, onde o elemento assume o valor de cada item da sequência em cada iteração.

Aqui está um exemplo simples para ilustrar o uso do loop for:
```
frutas = ["maçã", "banana", "laranja"]

for fruta in frutas:
    print(fruta)

print("Loop concluído")

```
Neste exemplo, temos uma lista de frutas e queremos imprimir cada uma delas. Utilizamos o loop for para percorrer a lista frutas. A cada iteração, o elemento atual da lista é atribuído à variável fruta, e imprimimos o valor dessa variável. Após o término do loop, a mensagem "Loop concluído" é exibida.

A saída para este exemplo será:

```
maçã
banana
laranja
Loop concluído

```

Você também pode usar a função range() junto com o loop for para iterar um número específico de vezes. A função range() retorna uma sequência de números e é comumente usada com o loop for para criar um loop com um número fixo de iterações.

Aqui está um exemplo:

```
for i in range(5):
    print(i)

print("Loop concluído")
```

Neste exemplo, usamos range(5) para criar uma sequência de números de 0 a 4. O loop for itera sobre esses números e os imprime. Após o término do loop, a mensagem "Loop concluído" é exibida.

A saída será:

```
0
1
2
3
4
Loop concluído

```

### - Aula 14 -  Estrutura de repetição while

A estrutura de repetição while em Python é usada para repetir um bloco de código enquanto uma condição específica for verdadeira. Ao contrário do loop for, que itera sobre uma sequência predefinida, o loop while continua executando até que a condição especificada seja avaliada como falsa.

A sintaxe básica do loop while é a seguinte:
```
while condição:
    # Código a ser executado enquanto a condição for verdadeira
```
O bloco de código dentro do while será repetido até que a condição seja avaliada como falsa. É importante garantir que haja uma condição dentro do loop que eventualmente se torne falsa, caso contrário, o loop continuará executando indefinidamente, resultando em um "loop infinito".

Aqui está um exemplo simples para ilustrar o uso do loop while:

``` 
contador = 0

while contador < 5:
    print("O contador é", contador)
    contador += 1

print("Loop concluído")

```
Neste exemplo, inicializamos a variável contador com o valor 0. O loop while continuará executando enquanto o valor do contador for menor que 5. A cada iteração do loop, o valor atual do contador é impresso na tela e, em seguida, incrementamos o valor do contador em 1. O loop continuará executando até que o contador atinja o valor 5, momento em que a condição se tornará falsa e o loop será encerrado. Após o término do loop, a mensagem "Loop concluído" é exibida.

A saída desse exemplo será:

```
O contador é 0
O contador é 1
O contador é 2
O contador é 3
O contador é 4
Loop concluído

```

# Mundo 3 
## Aula 16 - Tuplas 
```
Nessa aula, vamos aprender o que são TUPLAS e como utilizar tuplas em Python.
As tuplas são variáveis compostas e imutáveis que permitem armazenar vários valores em uma mesma estrutura,3
acessíveis por chaves individuais.
```

### Exemplo de como usamos as tuplas:
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

### Listas:
```
 Nessa aula, vamos aprender o que são LISTAS e como utilizar listas em Python.
 As listas são variáveis compostas que permitem armazenar vários valores em uma mesma estrutura,
 acessíveis por chaves individuais.
```
uma diferença entre tuplas e listas são:
Tuplas |  Listas
:---: | ---:  
são imutável|são mutáveis 

Obs: Click [Aqui](https://www.youtube.com/watch?v=N1hTsbW50eM) para acessar essa aula

## Primeiros passos usando lista :
 
### Comando append: 
```
É usado para adicionar algo a lista

# Ex:

Lanche = ['hamburguer', suco', 'pizza', 'picole']
Lanche.append(' cookie ')
Resultado:

Lanche = ['hamburguer', suco', 'pizza', 'picole', ' cookie ']  
  
# Insert:

 Usamos o comando INSERT quando queremos adicionar um item antes/depois de outro.

# Ex:

   Lanche.insert(0,'Cachorro-Quente')
   
   Obs: Acima estamos indicando a posição que queremos que o "cachorro-quente" fique.

 O resultado dessa alteração é

   Lanche = ['Cachorro-Quente', 'hamburguer', suco', 'pizza', 'picole', ' cookie '] 
```   
### Comandos para apagar um item da lista:


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

#

