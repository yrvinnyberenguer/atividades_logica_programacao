if __name__ == '__main__':
    A = int(input("Digite o valor inicial da PG: "))
    R = int(input("Digite a razão da PG: "))
    for i in range(10):
        print(A * (R ** i))
