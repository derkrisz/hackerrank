# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

shoes = int(input())
stock = Counter(map(int, input().split()))
customers = int(input())

total = 0

for _ in range(customers):
    size, price = map(int, input().split())
    if stock[size]:
        total += price
        stock[size] -= 1
        
print(total)
