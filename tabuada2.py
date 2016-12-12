for linha in range(2):
    for fator in range(10):
        for coluna in range(5):
            x = fator + 1
            y = coluna + 1 + 5*linha
            print('%2d x %2d = %3d     ' % (x, y, x*y), end='')
        print()
    print()