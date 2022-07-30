#dictionaries and maps
a=[]
n=int(input())
d=dict()
for i in range(n):
    NameNum=str(input())
    NameNum=NameNum.split(" ")
    d[NameNum[0]]=NameNum[1]
    
while True:
    s=str(input())
    if s=="":
        break
    else:
        if s in d.keys():
            print(s+"="+d[s])
        else:
            print("Not found")


#solution for EOF error 
a=[]
n=int(input())
d=dict()
for i in range(n):
    NameNum=str(input())
    NameNum=NameNum.split(" ")
    d[NameNum[0]]=NameNum[1]
    
while True:
    try:
        name=input()
    except EOFError:
        break
    if name=="":
        break
    else:
        if name in d.keys():
            print(name+"="+d[name])
        else:
            print("Not found")

