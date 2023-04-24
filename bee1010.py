if __name__ == '__main__':
 codigo_1 = int(input("DIgite o codigo da peça 1:"))
 numero_pecas_1 = int(input("Digite a quantidade de peças 1:"))
 valor_1 = float(input("DIgite o valor unitario da peça 1:"))
 codigo_2 = int(input("DIgite o codigo da peça 2:"))
 numero_pecas_2 = int(input("Digite a quantidade de peças 2:"))
 valor_2 = float(input("DIgite o valor unitario da peça 2:"))
 PAGAR = (numero_pecas_1 * valor_1 + numero_pecas_2 * valor_2)
 print("VALOR A PAGAR: R$ {:.2f}" .format(PAGAR))