#include<stdio.h>
int main()
{
int n,x,y;
scanf("%d\n%d %d",&n,&x,&y);
for(int i=1;i<n;i++)
{
    if(i%y!=0&& i==6)
    {
        printf("%d ",i*x);
    }
}
}