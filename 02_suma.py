m, n  = map(int, input().split())

# Jei m didesnis už n – sukeičiam vietomis
if m > n:
    m, n = n, m

# kraštiniai skaičiai nėra įtraukti
skaiciai_intervale = range(m + 1, n)

# norint peržiūrėti tarpinį rezultatą (skaičius sumai rasti) naudokite
# print(list(skaiciai_intervale))

print(sum(skaiciai_intervale))