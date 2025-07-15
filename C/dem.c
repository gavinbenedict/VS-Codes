#include<stdio.h>
#include<stdlib.h>

int main()
{
    int n, temp = 0;
    scanf("%d", &n);
    int b[n];
    for(int i = 0; i < n; i++)
    {
        scanf("%d", &b[i]);
    }
    for(int i = 0; i < n - 1; i++)
    {
        for(int j = 0; j < n - 1 - i; j++)
        {
            if(b[j] < b[j + 1])
            {
                temp = b[j];
                b[j] = b[j + 1];
                b[j + 1] = temp;
            }
        }
    }
    printf("%d", b[1]);  // ✅ second largest element after descending sort
    return 0;
}
