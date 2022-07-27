//loops
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
    int userInput,times,result;
    scanf("%d",&userInput);
    if(userInput>=2&&userInput<=20)
    {
        for(times=1;times<=10;times++)
        {
            result=userInput*times;
            printf("%d x %d = %d\n",userInput,times,result);
         }
    }
    return 0;
}
