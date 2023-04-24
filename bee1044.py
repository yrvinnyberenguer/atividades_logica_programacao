if __name__ == '__main__':
    A = int(input("Digite um valor para A: "))
    B = int(input("Digite um valor para B: "))
    if A % B == 0 or B % A == 0:
        print("Sao multiplos")
    else:
        print("Nao sao multiplos")
