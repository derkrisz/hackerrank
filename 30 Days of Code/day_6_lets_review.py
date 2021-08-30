# Enter your code here. Read input from STDIN. Print output to STDOUT

odds = ""
evens = ""
cases = int(input())

for _ in range(cases):
    odds = evens = ""
    for pos, char in enumerate(input()): 
        if pos % 2 == 0:
            evens += char
        else:
            odds += char
    print(evens, odds)
   