#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    c=0
    for i in range(n-1):
        for j in range(n-1):
            if j+1<n:
                if a[j]>a[j+1]:
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
                    c+=1

    print("Array is sorted in",c,"swaps.")
    print("First Element:",a[0])
    print("Last Element:",a[n-1])
                
