#array
if __name__ == '__main__':
    n = int(input().strip())
    a=str()
    b=str()
    arr = list(map(int, input().rstrip().split()))
    print(*arr[::-1])
