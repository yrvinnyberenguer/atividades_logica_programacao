if __name__ == '__main__':
    soma = 0
    pos = 0
    neg = 0
while True:
    numero = float(input(" Digite um numero: "))
    if numero == 0:
breakpoint
    soma += numero

    if numero > 0:
        pos += 1
    else numero < 0:
        neg += 1
total = pos + neg
media = soma / total

print("A média dos valores é {}" .format(media))
print("A quantidade de valores positivos é {}" .format(pos))
print("A quantidade de valores negativos é {}" .format(neg))