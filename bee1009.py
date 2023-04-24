if __name__ == '__main__':
 Nome = str(input("Digite seu nome:"))
 Sal_fixo = float(input("Digite seu salario fixo:"))
 total_vendas_mes = float(input("Insira seu total de vendas no mês em dinheiro:"))
 comissao = total_vendas_mes * 0.15
 print("TOTAL = R$ {:.2f}" .format(comissao))

