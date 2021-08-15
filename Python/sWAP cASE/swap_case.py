def swap_case(s):
    return "".join([l.lower() if l.isupper() else l.upper() for l in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)