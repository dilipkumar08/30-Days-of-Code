#conditional Statements
if __name__ == '__main__':
    N = int(input().strip())
    if N%2==1:
        print("Weird")
    elif 2<N<=5:
        print("Not Weird")
    elif 6<N<=20:
        print("Weird")
    elif N>20:
        print("Not Weird")
