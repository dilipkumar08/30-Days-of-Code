if __name__ == '__main__':
    S = input()
   
    try: 
        print(int(S))
    except: 
        print ("Bad String")


#Incase you getting this error message "Error reading result file.You should use exception handling concepts."
#use this below code as it is without 'if __name__ == '__main__':'

S = input().strip()
try: 
    print(int(S))
except: 
    print ("Bad String")
