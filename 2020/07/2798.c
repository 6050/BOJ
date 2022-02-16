#include <stdio.h>

int main()
{
    int cards[100];

    int num, m;
    scanf("%d %d", &num, &m);

    for ( int i = 0; i < num; i++ )
        scanf("%d", &cards[i]);
   

    int sum = 0, max = 0;
    for ( int i = 0; i < num; i++ )
    {
        for ( int j = i + 1; j < num; j++ )
        {
            for ( int k = j + 1; k < num; k++ )
            {

                sum = cards[i] + cards[j] + cards[k];
                if ( sum > max && sum <= m )
                    max = sum;
            }
        }
    }

    printf("%d\n", max);

    return 0;
}
