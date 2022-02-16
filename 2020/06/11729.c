#include <stdio.h>

void hanoi(int n, int from, int by, int to)
{
    if ( n == 1 )
        printf("%d %d\n", from, to);
    else
    {
        hanoi(n - 1, from, to, by);
        printf("%d %d\n", from, to);
        hanoi(n - 1, by, from, to);
    }
}

int main()
{
    int num;
    scanf("%d", &num);

    int count = 1;
    for ( int i = 0; i < num; i++ ) count *= 2;
    count -= 1;

    printf("%d\n", count);
    hanoi(num, 1, 2, 3);

    return 0;
}
