n = int(input())
matrica = []
for i in range(n):    
    matrica.append(list(map(int, input().split())))

# # fake data
# n = 3
# matrica = [[1, 5, 9], [4, 3, 6], [2, 8, 7]]

# n = 4
# matrica = [[15, 2, 12, 4], [1, 14, 10, 5], [8, 9, 3, 16], [11, 13, 6, 7]]

sumos = []
for i in range(n):
    # konteineris stulpelio sumai
    sumos.insert(i, 0)

    # eilutės i suma
    sumos.append(sum(matrica[i]))
    
    istrizaines_suma1 = 0
    istrizaines_suma2 = 0
    for j in range(n):
        sumos[i] += matrica[j][i]

        if i == (n - 1):
            istrizaines_suma1 += matrica[j][j]
            istrizaines_suma2 += matrica[j][n - j - 1]

sumos.append(istrizaines_suma1)
sumos.append(istrizaines_suma2)

sumos.sort()

# tikrinama ar sumos eina iš eillės
antimagiskas = True
for i in range(1, len(sumos)):
    if sumos[i - 1] + 1 != sumos[i]:
        antimagiskas = False
        break

# print(matrica)
# print(sumos)

if antimagiskas:
    print(sumos[0], sumos[len(sumos) - 1], sep=" ")
else:
    print(0)