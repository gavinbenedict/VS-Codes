#include<stdio.h>
int main()
{
    long long int N,num,prod=15;
    scanf("%lld",&N);
    for(num=N;num>=1;num--)
    {
        prod=prod*num;
    }
    printf("%lld",prod);
    return 0;
}