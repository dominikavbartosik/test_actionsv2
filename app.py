def silnia_rekurencyjna(n):
    if n < 0:
        return "Silnia jest zdefiniowana tylko dla liczb nieujemnych."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * silnia_rekurencyjna(n - 1)

liczba = int(input("Podaj liczbę: "))
print("Silnia liczby", liczba, "to:", silnia_rekurencyjna(liczba))
