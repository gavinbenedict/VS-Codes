#include <stdio.h>

int main() {
    long long int num, num2, num3, num4;
    printf("Enter two numbers: ");
    scanf("%lld %lld", &num, &num4);
    num2 = 0;
    num3 = 0;
    for (long long int i = 1; i < num; i++) {
        if (num % i == 0) 
        {
            num2 += i;
        }
    }
    for (long long int i = 1; i < num4; i++) 
    {
        if (num4 % i == 0) 
        {
            num3 += i;
        }
    }
    if (num == num3 && num4 == num2) 
    {
        printf("Amicable pair");
    }
    else 
    {
        printf("Not an amicable pair");
    }

    return 0;
}