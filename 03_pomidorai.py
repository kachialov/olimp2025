n, m, d  = map(int, input().split())

prinokiusiu_skaicius = 1
liko_desineje = n - m
liko_kaireje = n - liko_desineje - 1
for i in range(d):
    if liko_kaireje > 0:
        prinokiusiu_skaicius += 1
        liko_kaireje -= 1
    if liko_desineje > 0:
        prinokiusiu_skaicius += 1
        liko_desineje -= 1

    if liko_kaireje < 1 and liko_desineje < 1:
        break

print(n - prinokiusiu_skaicius)