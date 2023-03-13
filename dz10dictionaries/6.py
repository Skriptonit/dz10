d = {}
d1= {}
for j in range(int(input())):
  for i in input().split():
    d[i] = d.get(i, 0) + 1
for key, val in d.items():
  d1[val]=key
for i in sorted(d1.keys(), reverse=True):
  for j in sorted(d.keys()):
    if d[j]==i:
      print(j)