dias = int(input())

ano = dias // 365
resto1 = dias % 365
mes = resto1 // 30
dias = resto1 % 30

	
print('{} ano(s)'.format(ano))
print('{} mes(es)'.format(mes))
print('{} dia(s)'.format(dias))
