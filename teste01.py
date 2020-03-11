valor_litros = float(input('qual o valor do litros:'))
valor_reais = float(input('quanto quer abastecer:'))
litros = valor_reais / valor_litros
print('com R %.2f o veiculo vai receber %.2f litros.' % (valor_reais, litros))
