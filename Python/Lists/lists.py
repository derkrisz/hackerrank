if __name__ == '__main__':
    N = int(input())
    
list = []

for i in range(N):
    ip = input().split()
    command = ip[0]
    if command == "insert":
        list.insert(int(ip[1]), int(ip[2]))
    elif command == "print":
        print(list)
    elif command == "remove":
        list.remove(int(ip[1]))
    elif command == "append":
        list.append(int(ip[1]))
    elif command == "sort":
        list.sort()
    elif command == "pop":
        list.pop()
    elif command == "reverse":
        list.reverse()
        
