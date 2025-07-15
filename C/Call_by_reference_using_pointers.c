#include<stdio.h>
void diddy(int *x,int *y)
{
        int temp=*x;
        *x=*y;
        *y=temp;
        
}
int main()
{
    int a=5,b=10;
    printf("%d %d\n",a,b);
    diddy(&a,&b);
    printf("%d %d",a,b);
    return 0;
}