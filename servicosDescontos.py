print('Olá, seja bem-vindo ao serviço de descontos da Loja do Rodrigo Alcantara') #Print de boas-vindas

valor = float(input('Qual o valor unitário do produto que está levando?\n')) #Entrada da primeira variável com o valor
qtd = int(input('Qual a quantidade de produtos que está levando?\n')) #Entrada da segunda variável com a quantidade
total = valor * qtd #Valor total sem descontos

if total >= 10000: #Se valor maior que 10000 multiplica o valor por 0,89
    print(f'Sua compra ficará no total de R${total:.2f}, mas você tem direito a 11% de desconto.\nTotal à pagar com desconto R${total * 0.89 :.2f}')
elif total >= 6000: #Se valor maior que 6000 multiplica o valor por 0,93
    print(f'Sua compra ficará no total de R${total:.2f}, mas você tem direito a 7% de desconto.\nTotal à pagar com desconto R${total * 0.93 :.2f}')
elif total >= 2500: #Se valor maior que 2500 multiplica o valor por 0,96
    print(f'Sua compra ficará no total de R${total:.2f}, mas você tem direito a 4% de desconto.\nTotal à pagar com desconto R${total * 0.96 :.2f}')
else: #Se nenhuma das condições for aplicada, envia o valor sem desconto
    print(f'Sua compra ficará no total de R${total:.2f}, considere levar mais produtos para garantir descontos!')