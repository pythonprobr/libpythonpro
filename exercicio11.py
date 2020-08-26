"""
Programa para calcular reajuste de salário.

Parametros: salário
Return: reajuste

Critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5%

Após o aumento ser realizado,
informe na tela:

o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
"""


salario = float(input('Digite seu salario: '))

faixas = {'f1': 0.2, 'f2': 0.15, 'f3': 0.1, 'f4': 0.05}


def calcula_aumento(salario):
    """Retorna taxa e aumento."""
    if salario <= 280:
        taxa = faixas['f1']
    elif salario < 700:
        taxa = faixas['f2']
    elif salario < 1500:
        taxa = faixas['f3']
    elif salario >= 1500:
        taxa = faixas['f4']

    aumento = salario * taxa

    return taxa, aumento


taxa, aumento = calcula_aumento(salario)

print(f'Salário antes ddo reajuste é R$ {salario}')
print(f'Percentual de aumento {taxa * 100}%')
print(f'Valor do aumento: R$ {aumento}')
print(f'Novo salário: R$ {salario + aumento}')
