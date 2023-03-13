n = {}
for i in range(int(input())):
    a = input().split()
    for k in a:
        n[k] = n.get(k, 0) + 1

max_n = max(n.values())
most_frequent = [k for k, v in n.items() if v == max_n]
print(min(most_frequent))