# 🛍️ Serviço de Descontos – Loja do Rodrigo Alcantara
Este é um programa simples desenvolvido em **Python** que simula um sistema de descontos progressivos em uma loja, com base no valor total da compra.

## 💻 Tecnologias utilizadas
- Linguagem Python 3
- Terminal/Console

## ⚙️ Funcionalidades
- Entrada do valor unitário do produto
- Entrada da quantidade de produtos
- Cálculo do valor total
- Aplicação de descontos baseados no valor da compra:
  - 11% de desconto para compras a partir de R$10.000,00
  - 7% de desconto para compras a partir de R$6.000,00
  - 4% de desconto para compras a partir de R$2.500,00
  - Sem desconto para valores inferiores

## ▶️ Como executar
1. Copie o código para um arquivo `.py`, por exemplo: `descontos.py`
2. Execute o programa em um terminal com o comando:
```bash
python descontos.py
```

## 📝 Exemplo de uso
```bash
Olá, seja bem-vindo ao serviço de descontos da Loja do Rodrigo Alcantara
Qual o valor unitário do produto que está levando?
1000
Qual a quantidade de produtos que está levando?
10
Sua compra ficará no total de R$10000.00, mas você tem direito a 11% de desconto.
Total à pagar com desconto R$8900.00
```

## 📌 Observações
- O programa aceita **valores decimais** para o preço do produto.  
- Os cálculos de desconto são baseados no **valor total da compra**.  
- Os descontos são aplicados por **faixas de valor**: quanto maior a compra, maior o desconto.  
- Recomendado executar em **terminal compatível com entrada e saída padrão** do Python.