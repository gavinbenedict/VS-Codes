#include<stdio.h>
int main()
{
    long long int i,num;
    printf("Enter a number: ");
    scanf("%lld",&num);
    for(i=0;i<=num;i++)
    {
        if(num%i==0)
        {
            printf("[%lld] ",i);

        }
    }
    return 0;
}