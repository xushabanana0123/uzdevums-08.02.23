#2. Izveidot funkciju, kas izdrukā no patvaļīgi izveidota saraksta tikai nepāra skaitļus.
def funkcija(sar1):
  for x in sar1:
    if x%2 == 0:
      print(x)
  return 0
sar1 = [1,5,4,2,3,4,1,2,5]
funkcija(sar1)