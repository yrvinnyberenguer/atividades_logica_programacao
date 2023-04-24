if __name__ == '__main__':
    intervalo_1 = 0
    intervalo_2 = 0
    intervalo_3 = 0
    intervalo_4 = 0
 while True:
    numero = int(input("Digite um número (digite um número negativo para sair): "))
    if numero < 0:
breakpoint
         if numero >= 0 and numero <= 25:
            intervalo_1 += 1
        elif numero >= 26 and numero <= 50:
            intervalo_2 += 1
        elif numero >= 51 and numero <= 75:
            intervalo_3 += 1
        elif numero >= 76 and numero <= 100:
            intervalo_4 += 1

    print("Quantidade de números no intervalo [0-25]: {}".format(intervalo_1))
    print("Quantidade de números no intervalo [26-50]: {}".format(intervalo_2))
    print("Quantidade de números no intervalo [51-75]: {}".format(intervalo_3))
    print("Quantidade de números no intervalo [76-100]: {}".format(intervalo_4))
