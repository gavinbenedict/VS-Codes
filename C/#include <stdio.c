#include <stdio.h>
int main()
{
    int a;
    printf("Enter : \n");
    scanf("%d",&a);
    switch(a)
    {
        case '0':
        {
            printf("HI");
        }
        break;

        case '1':
        {
            printf("HELLO");
        }
        break;
        
        case '3':
        {
            printf("COMPUTER");
        }
        break;
        
        default:
        {
            printf("default");
        }
    }
    return 0;

}