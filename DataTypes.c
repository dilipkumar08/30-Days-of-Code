#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
    int i = 4;
    double d = 4.0;
    char s[] = "HackerRank ";
int userInt;
double userDouble;
char userChar[100];
scanf("%d%lf",&userInt,&userDouble);
getchar();
scanf("%[^\n]s",userChar);
i=i+userInt;
d=d+userDouble;
printf("%d\n%.1lf\n%s%s",i,d,s,userChar);

    return 0;
    }
