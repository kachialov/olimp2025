n = int(input())
kortu_skaiciai = []
kortu_tipai = []
for i in range(n):    
    sk, t = map(int, input().split())
    kortu_skaiciai.append(sk)

    if t == 1:
        t = 1000
    elif t == 4:
        t = 100
    elif t == 3:
        t = 10

    kortu_tipai.append(t)

# n = 22
# kortu_skaiciai = [10, 1, 7, 1, 1, 3, 1, 15, 8, 3, 5, 3, 2, 1, 1, 1, 1, 2, 2, 6, 8, 3]
# kortu_tipai = [1000, 1, 10, 100, 100, 1000, 1, 1000, 1000, 1000, 1000, 1000, 1, 10, 100, 100, 10, 1000, 10, 1, 1000, 100]

aldas = 0
martynas = 0
lygiosios = 0

for i in range(0, n, 10):
    if n - i < 10:
        break

    aldo_kortos = kortu_skaiciai[(i):(i + 5)]
    martyno_kortos = kortu_skaiciai[(i + 5):(i + 10)]

    aldo_sum = sum(aldo_kortos)
    martyno_sum = sum(martyno_kortos)
    aldo_max = max(aldo_kortos)
    martyno_max = max(martyno_kortos)

    if aldo_sum > martyno_sum:
        aldas += 1
    elif aldo_sum < martyno_sum:
        martynas += 1
    elif aldo_max > martyno_max:
        aldas += 1
    elif aldo_max < martyno_max:
        martynas += 1
    else:
        aldo_tipu_svoris = sum(kortu_tipai[(i):(i + 5)])
        martyno_tipu_svoris = sum(kortu_tipai[(i + 5):(i + 10)])

        if aldo_tipu_svoris > martyno_tipu_svoris:
            aldas += 1
        elif aldo_tipu_svoris < martyno_tipu_svoris:
            martynas += 1
        else:
            lygiosios += 1


print(aldas)
print(martynas)
print(lygiosios)