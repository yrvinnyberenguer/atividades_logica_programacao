if __name__ == '__main__':
    a = float(input("Digite valor para a: "))
    b = float(input("Digite valor para b: "))
    c = float(input("Digite valor para c: "))
    while True:
        perimetro = a + b + c
        print("{:.1f}" .format(perimetro))
    else:
        area_trap = (a + b) * c / 2
        print("{:.1f}" .format(area_trap))