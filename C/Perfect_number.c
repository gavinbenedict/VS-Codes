#include<stdio.h>
int main()
{
    long long int i,num,num2=0;
    printf("Enter a number: ");
    scanf("%lld",&num);
    for(i=0;i<num;i++)
    {
        if(num%i==0)
        {
            num2+=i;
        }
        
    }
    printf("%lld ",num2);
    if(num2==num)
    {
        printf("is a perfect number");
    }
    else 
    {
        printf("is NOT a perfect number");
    }
    return 0;
}