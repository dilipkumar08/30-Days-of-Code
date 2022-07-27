#include<stdio.h>
#include<conio.h>
int main()
{
    double mealCost,tax,tips;
    int fmc;
    clrscr();
    scanf("%lf%lf%lf",&mealCost,&tax,&tips);
    tax=(tax*mealCost)/100;
    tips=(tips*mealCost)/100;
    fmc=mealCost+tips+tax;
    printf("%d",fmc);
    getch();
    return 0;    
    
}
