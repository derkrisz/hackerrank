# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int,input().split())

a = defaultdict(list)

for i in range(n):
    a[input()].append(i + 1)
    
for i in range(m):
    #key = input()
    #if len(a[key]) > 0:
    #    print(" ".join(str(c) for c in a[key]))
    #else:
    #    print(-1)
    print(*a[input()] or [-1])
