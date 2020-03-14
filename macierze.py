# podać ile na ile jest macierz
# kiedy macierz nie może być pomnożona
# UZUPELNIĆ macierze
# pomnożyć macierze 
# wypisać wynik
# zadeklarować macierze

rozmiar_Ax = input("Podaj wysokość macierzy A=")
print(rozmiar_Ax)

rozmiar_Ay = input("Podaj szerokość macierzy A=")
print(rozmiar_Ay)

rozmiar_Bx = input("Podaj wysokość macierzy B=")
print(rozmiar_Bx)

rozmiar_By = input("Podaj szerokość macierzy B=")
print(rozmiar_By)

if rozmiar_Ay != rozmiar_Bx:
    print("Nie można pomnożyć!")
    exit(-1)

row_A = int(rozmiar_Ax)
col_A =int(rozmiar_Ay)
row_B = int(rozmiar_Bx)
col_B = int(rozmiar_By)

macierz_A = [[0 for col in range(col_A)] for row in range(row_A)]

for row in range(row_A):
    for col in range(col_A):
        macierz_A[row][col]= float(input("Macierz A, kolumna {0}, wiersz {1} =".format(col, row)))

print(macierz_A)

macierz_B = [[0 for col in range(col_B)] for row in range(row_B)]

for row in range(row_B):
    for col in range(col_B):
        macierz_B[row][col]= float(input("Macierz B, kolumna {0}, wiersz {1} =".format(col, row)))

print(macierz_B)


macierz_C = [[0 for col in range(col_B)] for row in range(row_A)]

for row in range(row_A):
    for col in range(col_B):
        suma = 0
        for i in range(col_A):
            suma += macierz_A[row][i] * macierz_B[i][col]
        macierz_C[row][col]= suma

print(macierz_C)