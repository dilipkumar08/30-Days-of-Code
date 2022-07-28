#recursion
def factorial(n):
    i=1
    b=1
    while i<=n:
        b=i*b
        i=i+1
    return b

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
