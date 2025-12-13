n, k  = map(int, input().split())
pavardes = []
for i in range(n):
    pavardes.append(input())

# # fake data input
# n, k = 7, 2
# pavardes = ["amstrong", "ashley", "narbutis", "paris", "smith", "watson",  "wilson"]
# n, k = 6, 5
# pavardes = ["grant" ,"house" ,"lucas" ,"nesby" ,"nielsen" ,"woodberry"]

didziausias_kiekis = 0
kiekis = 0
raide = ""

for i in range(n):
    pirmoji_raide = pavardes[i][0]
 
    # naujas puslapis
    if i % k == 0:
        if didziausias_kiekis < kiekis:
            didziausias_kiekis = kiekis
        # Pradėdame iš naujo ir pirmo patikrinimo (if raide != pirmoji_raide) nereikia, todėl (kiekis = 1)
        kiekis = 1
        raide = pirmoji_raide

    if raide != pirmoji_raide:
        raide = pirmoji_raide
        kiekis += 1

# paskutinio puslapio patikra
if didziausias_kiekis < kiekis:
            didziausias_kiekis = kiekis

print(didziausias_kiekis)