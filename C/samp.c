//prgrm: to convert timei
#include <stdio.h>
int main()
{
    int t,hrs,sec,min;
    printf("Enter time in seconds :\n");
    scanf("%d",&t);
    hrs=t/3600;
    sec=(t%3600)/60;
    min=((t%3600)/60)%60;
    printf("%d:%d:%d",hrs,min,sec);
    return 0;
}