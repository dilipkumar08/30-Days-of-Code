#include <assert.h>
#include <limits.h>
#include <math.h>
#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char* readline();
int main()
{
int userInput,modulus;
scanf("%d",&userInput);
modulus=userInput%2;
if(userInput<=100&&userInput>=1)
    {
        if(modulus==1)
        {
        printf("Weird");
        }   
            else if(userInput>=2&&userInput<=5)
            {
            printf("Not Weird");
            }
            else if(userInput>=6&&userInput<=20)
            {
            printf("Weird");    
            }   
            else
            {
            printf("Not Weird"); 
        }
    }
 return 0;
}
