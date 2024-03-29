import sys

class Solution:
    def __init__(self):
        self.stack=list()
        self.queue=list()
        return None
    def pushCharacter(self,inp):
        self.stack.append(inp)
    def enqueueCharacter(self,inp):
        self.queue.append(inp)
    def popCharacter(self):
        return (self.stack.pop(-1))
    def dequeueCharacter(self):
        return (self.queue.pop(0))
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
