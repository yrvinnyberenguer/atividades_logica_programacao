if __name__ == '__main__':
    n = int(input("Insira um numero de tabuada: "))
    if n > 1 and n < 10:
        print("Tabuada de {}" .format(n))
    else:
        print("O valor deve estar entre 1 e 10")
for i in range (1,11):
    print("{} * {} = {}" .format(n, i, n*i))
