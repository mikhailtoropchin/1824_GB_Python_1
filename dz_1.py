from heapq import heapreplace


p = [(0, i) for i in range(int(input().split()[0]))]

for x in map(int, input().split()):
    print(*reversed(heapreplace(p, (p[0][0] + x, p[0][1]))))

