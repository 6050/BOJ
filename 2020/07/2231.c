#include <stdio.h>

int main()
{
    int num;
    scanf("%d", &num);

    for ( int i = 1; i < num; i++ )
    {
        int sum = i, divide = i;
        
        while ( divide )
        {
            sum += divide % 10;
            divide /= 10;
        }

        if ( num == sum )
        {
            printf("%d\n", i);
         
            return 0;
        }
    }

    printf("0\n");

    return 0;
}
