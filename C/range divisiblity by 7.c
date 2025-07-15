#include<stdio.h>
void main()
{
int x,y; 
scanf ("%d",&х);
scanf ("%d",&у);
int count=0;
for(int i=x;i<=y;i++)
{
    if(i%2!=0&&i%7==0)
    {
        count++;
    }
}
printf("%d",count);
return 0;
}