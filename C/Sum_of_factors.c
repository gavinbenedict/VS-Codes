#include<stdio.h>
int main()
{
    long long int i,num,num2=0;
    printf("Enter a number: ");
    scanf("%lld",&num);
    for(i=0;i<=num;i++)
    {
        if(num%i==0)
        {
            printf("[%lld] ",i);
            num2=num2+i;
        }
        
    }
    printf("\nSum of factors: ");
    printf("%lld",num2);
    return 0;
}