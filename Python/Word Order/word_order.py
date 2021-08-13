# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

od = OrderedDict()

for i in range(int(input())):
    key = input()
    od[key] = od.get(key, 0) + 1
    #if od.get(key):
    #    od[key] += 1
    #else:
    #    od[key] = 1
        
print(len(od), " ".join(list(map(str, od.values()))), sep='\n')