#Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time do Flamengo.

Campeonato = ('Botafogo', 'Palmeiras', 'São Paulo', 'Atlético-MG', 'Grêmio', 'Cruzeiro', 'Framengo', 'Flamengo', 'Fluminense','Fortaleza','Bragantino','Athletico-PR', 'Santos', 'Internacional','Corinthias','Cuiabá', 'Bahia', 'Goiás','Vasco','Améririca-Mg','Coritiba')

print(f'Os 5 primeiros times são: {Campeonato[0:6]}')
print('====' * 40)
print(f'Os 4 últimos colocados são {Campeonato[-4]}')
print('====' * 40)
Ordem_Nome = sorted(Campeonato)
print(f'A ordem alfabética dos times é {Ordem_Nome}')
print('====' * 40) 
posicao_flamengo = Campeonato.index('Flamengo') + 1
print(f'O Flamengo está na {posicao_flamengo}ª posição.')