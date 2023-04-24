if __name__ == '__main__':
    A = float(input("Digite o valor de A: "))
    B = float(input("Digite o valor de B: "))
    C = float(input("Digite o valor de C: "))
    pi = 3.14159
    area_tri = (A * C) / 2
    area_circ = pi * C**2
    area_trap = (A + B) * C / 2
    area_quad = B * B
    area_ret = A * B
    print("TRIANGULO: {:.3f}" .format(area_tri))
    print("CIRCULO: {:.3f}".format(area_circ))
    print("TRAPEZIO: {:.3f}".format(area_trap))
    print("QUADRADO: {:.3f}".format(area_quad))
    print("RETANGULO: {:.3f}" .format(area_ret))

