n = int(input())
d = {}
for i in range(n):
    a, b = input().split()
    d[a] = b
    d[b] = a
print(d[input()])
