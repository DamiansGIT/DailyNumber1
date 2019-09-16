from funkcja_szukajaca_sumy import szukanie_sumy


numbers = [ 10, 20, 15, 8, 3, 17, 2, 5]

sum_value = input('Podaj wartość szukanej sumy: ')


wynik = szukanie_sumy(numbers, sum_value)

print("Wynik funkcji to " + str(wynik))

