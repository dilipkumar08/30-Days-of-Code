#2d arrray
if __name__ == '__main__':

    arr = []
    b=[]
    res=[]
    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    for i in range(0,4):
        for j in range(0,4):
            s=sum(arr[i][j:j+3])
            b.append(s)
            s=arr[i+1][j+1]
            b.append(s)
            s=sum(arr[i+2][j:j+3])
            b.append(s)
            res.append(sum(b))
            b.clear()
    print(max(res))
