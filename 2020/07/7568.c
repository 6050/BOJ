#include <stdio.h>
#include <stdlib.h>

int main()
{
    int num;
    scanf("%d", &num);

    int x[50] = { 0, };
    int y[50] = { 0, };

    for ( int i = 0; i < num; i++ )
        scanf("%d %d", &x[i], &y[i]);
 
    for ( int i = 0; i < num; i++ )
    {
        int grade = 1;
        for ( int j = 0; j < num; j++ )
        {
            if ( x[i] < x[j] && y[i] < y[j] )
                grade++;
        }
        printf("%d ", grade);
    }

    return 0;
}
