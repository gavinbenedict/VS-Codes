#include<stdio.h>
int main()
{
    int num;
    printf("Enter num value: ");
    scanf("%d",&num);
    if(num>=0 && num<=9)
    {
        printf("ONES");
    }
    else if(num>=10  &&  num<=99)
    {
        printf("TENS");
    }
    else if(num>=100 && num<=999)
    {
        printf("HUNDREDS");
    }
    else if (num>=1000 && num<=9999)
    {
        printf("THOUSANDS");
    }
    else
    {
        printf("INVALID ENTRY");;
    }
    return 0;
}