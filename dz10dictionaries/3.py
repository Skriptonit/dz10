d = {}
n = int(input())
for i in range(n):
    a, b = input().split()
    d[a] = d.get(a, 0) + int(b)

for a, b in sorted(d.items()):
    print(a, b)
