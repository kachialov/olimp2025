a, p = map(int, input().split())
gauti = list(map(int, input().split()))

# a, p = 3, 2
# gauti = [5, 3, 2]

# iеškosime pagal tvarką surašytą laiške
gauti.reverse()
iskritusiu_kiekis = 0
turejo_gauti = p

for i in range(a):
    zaidejas_gavo = gauti[i]

    if turejo_gauti > zaidejas_gavo:
        iskritusiu_kiekis += (turejo_gauti - zaidejas_gavo)

    if i < (a - 1):
        turejo_gauti = zaidejas_gavo * p
  
print(iskritusiu_kiekis)