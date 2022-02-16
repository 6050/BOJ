#include <stdio.h>

char map[3000][3000];

void stars(int x, int y, int n)
{
    if ( n == 1 )
    {
        map[x][y] = '*';
        return;
    }
    
    int num = n / 3;

    for ( int i = 0; i < 3; i++ )
    {
        for ( int j = 0; j < 3; j++ )
        {

            if ( i == 1 && j == 1 ) continue;
            else stars(x + (i*num), y + (j*num), num);

        }
    }
}

int main()
{
    int num;
    scanf("%d", &num);

    for ( int i = 0; i < 3000; i++ )
    {
        for ( int j = 0; j < 3000; j++ )
        {
            map[i][j] = ' ';
        }
    }

    stars(0, 0, num);
    
    for ( int i = 0; i < num; i++ )
    {
        for ( int j = 0; j < num; j++ )
            printf("%c", map[i][j]);
        printf("\n");
    }

    return 0;
}
