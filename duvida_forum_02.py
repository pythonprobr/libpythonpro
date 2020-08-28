contagem = ('zero', 'um', 'dois', 'três', 'quatro', 
            'cinco', 'seis', 'sete', 'oito', 'nove', 
            'dez', 'onze', 'doze', 'treze', 'quatorze', 
            'quinze', 'dezesseis', 'dezessete', 'dezoito', 
            'dezenove', 'vinte')

num = int(input('Digite um número de 0 à 20: '))

while num < 0 or num > 20:
    num = int(input('ERRO: Digite um número de 0 à 20:'))
    if num >= 0 and num <= 20:
        break
