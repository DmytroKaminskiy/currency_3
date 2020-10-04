group = ['uds', 2, 2, 0, 'eur', 3, 4, 0]
n = 4

res = [group[i:i + n] for i in range(0, len(group), n)]
print(res)
