for sayi in range(1, 101):
  print(sayi)
  for sayi in range(2, 101, 2):
  print(sayi)
  sayi = int(input("Bir sayı girin: "))

faktoriyel = 1
if sayi < 0:
    print("Negatif sayıların faktöriyeli hesaplanamaz.")
elif sayi == 0:
    print("0'ın faktöriyeli 1'dir.")
else:
    for i in range(1, sayi + 1):
        faktoriyel *= i
    print(f"{sayi}! = {faktoriyel}")
    for sayi in range(2, 101):
    asal_mi = True
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            asal_mi = False
            break
    if asal_mi:
        print(sayi)