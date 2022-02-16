#include <stdio.h>

int main()
{
    int num;
    scanf("%d", &num);

    for ( int i = 1; i <= num * 2; i++ )
    {
        for ( int j = 1; j <= num; j++ )
        {
            if ( i % 2 == 0 )
            {
                if ( j % 2 == 0 ) printf("*");
                else printf(" ");
            }
            else
            {
                if ( j % 2 == 0 ) printf(" ");
                else printf("*");
            }
        }
        
        printf("\n");
    }
}
