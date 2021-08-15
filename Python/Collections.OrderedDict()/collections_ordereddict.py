# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

ordered_dict = OrderedDict()

for _ in range(int(input())):
    item = input().split()
    price, name = int(item[-1]), ' '.join(item[:-1])
    
    ordered_dict[name] = ordered_dict.get(name, 0) + price
    
    #if ordered_dict.get(name):
    #    ordered_dict[name] += price
    #else:
    #    ordered_dict[name] = price   

for item, price in ordered_dict.items():
    print(item, price)
        
