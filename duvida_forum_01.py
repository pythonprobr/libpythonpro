bras = ('Internacional',
        'vasco',
        'São Paulo',
        'Atlético-MG',
        'Palmeiras',
        'Santos',
        'Fluminense',
        'Bahia',
        'Grêmio',
        'Atlético-PR',
        'Botafogo',
        'Corinthians',
        'Bragantino',
        'Fortaleza',
        'Flamengo',
        'Goías',
        'Atlético-GO',
        'Sport',
        'Ceará',
        'Coritiba')

escolha = (input(' Escolha um time : '))
print(f' Os primeiros 5 colocados são: {bras[0 : 5]}')
print(f' Os 4 últimos colocados na tabela são : {bras[-4:]}')
print(f' Os times em ordem alfabética são :{sorted(bras)}')
print(f' A posição do time que você escolheu é : {bras.index(escolha)}')
