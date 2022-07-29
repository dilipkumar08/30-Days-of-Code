#binary numbers
if __name__ == '__main__':
    n = int(input().strip())
    b=bin(n)
    b=b[2:]
    a=b.split("0")
    m=max(a)
    print(len(m))
