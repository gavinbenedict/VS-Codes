#include<stdio.h>
int main()
{
    int i,num,test;
    printf("Enter number: ");
    scanf("%d",&num);
    for(int i=0;i<num;i++)
    {
        if(num%i==0)
        {
            test=1;
            break;
        }
    }
    if(test==0)
    {
        printf("Prime number");
    }
    else
    {
        printf("Not a prime number");
    }
    return 0;
}