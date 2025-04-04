from __future__ import annotations

from src.libb import silnia_rekurencyjna


if __name__ == '__main__':
    liczba = int(input('Podaj liczbę: '))
    print('Silnia liczby', liczba, 'to:', silnia_rekurencyjna(liczba))
