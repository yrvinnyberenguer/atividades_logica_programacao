if __name__ == '__main__':
    N1 = float(input("Digite nota 1: "))
    N2 = float(input("Digite nota 2: "))
    N3 = float(input("Digite nota 3: "))
    N4 = float(input("Digite nota 4: "))
    media = (N1 * 2 + N2 * 3 + N3 * 4 + N4 * 1) / 4
    print("{:.1f}" .format(media))
    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado")
    exame = float(input("Digite a nota do exame:"))
    nova_media = media + exame / 2
    print("{:.1f}" .format(exame))
    if nova_media >= 5:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")