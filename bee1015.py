if __name__ == '__main__':
    x1 = float(input("Digite o valor de x1: "))
    y1 = float(input("Digite o valor de y1: "))
    x2 = float(input("Digite o valor de x2: "))
    y2 = float(input("Digite o valor de y2: "))
    distancia = ((x2 - x1)**2 + (y2 - y1)**2) ** (1/3)
    print("{:.4f}" .format(distancia))