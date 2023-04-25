'''Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Palmeiras.'''
from time import sleep

Times =  ('Fluminense', 'Botafogo', 'Fortaleza', 'Vasco', 'Palmeiras',
         'Internacional', 'Bragantino', 'São Paulo', 'Flamengo',
         'Goiás', 'Cruzeiro', 'Athletico-PR', 'Grêmio', 'Corinthians',
         'Cuiabá', 'Atlético-MG', 'Santos', ' Bahia', ' América-MG', 'Coritiba' )

print(f'lIsta de times do brasileirão: {Times}')
print('=' * 30)
sleep(1)
print(f'Os 5 primeiros times são {Times[0:5]}')
print('=' * 30)
sleep(1)
print(f'Os 4 ultimos colocados são {Times[-4:]}')
print('=' * 30)
sleep(1)
print(f'os times em ordem alfabética {sorted(Times)}')
print('=' * 30)
sleep(1)
print(f'O Palmeiras está na {Times.index("Palmeiras")+1}º posição')
