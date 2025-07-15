#include <stdio.h>
int add(int a,int b)
{
    int c,a1,b1;
    a1=a;
    b1=b;
    c=a1+b1;
    return c;
}
int subtract(int a,int b)
{
    int c,a1,b1;
    a1=a;
    b1=b;
    c=a1-b1;
    return c;
}
int multiply(int a,int b)
{
    int c,a1,b1;
    a1=a;
    b1=b;
    c=a1*b1;
    return c;
}
int divide(int a,int b)
{
    int c,a1,b1;
    a1=a;
    b1=b;
    c=a1/b1;
    return c;
}
int main() 
{
    printf("HI!\n\n1-ADD\n2-SUBTRACT\n3-multiply\n4-divide\n\nCHOOSE A NUMBER BASED ON THE ABOVE MENU:");
    int num;
    scanf("%d",&num);
    printf("ENTER 2 VALUES: ");
    int a,b;
    scanf("%d%d",&a,&b);
    switch(num)
    {
        case 1:printf("%d",add(a,b));
        break;
        case 2: printf("%d",subtract(a,b));
        break;
        case 3: printf("%d",multiply(a,b));
        break;
        case 4: printf("%d",divide(a,b));
        break;
        default:printf("INVALID ENTRY");
        break;
    }
    return 0;
}