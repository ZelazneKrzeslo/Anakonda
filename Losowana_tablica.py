import numpy as np 

print("Pierwsza Macierz")
x = input("Kolumny: ")
y = input("Wiersze: ")

x = int(x) 
y = int(y)

macierz_1 = np.random.randint(200, size=(y,x))
print(macierz_1)

print("Druga macierz: ")
a = input("Ile kolumn?: ")
b = input("Ile wierszy?: ")

a = int(a)
b = int(b)

macierz_2 = np.random.randint(200, size=(b,a))
print("Druga macierz: \n", macierz_2,"\n")

macierz_3 = macierz_1 + macierz_2
print("Macierz 1 i macierz 2 dodane do siebie: \n")
print(macierz_3, "\n")

macierz_4 = macierz_1 * macierz_2
print("Macierz 1 i macierz 2 pomnozone przez siebie: \n")
print(macierz_4)
