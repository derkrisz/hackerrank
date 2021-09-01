# Enter your code here. Read input from STDIN. Print output to STDOUT

dict_values = int(input())

phone_book = dict()

for _ in range(dict_values):
    name, phone = input().split()
    phone_book[name] = phone

while True:
    try:
        name = input()
        if name in phone_book:
            print(name, "=", phone_book[name], sep="")
        else:
            print('Not found')
    except:
        break
    
