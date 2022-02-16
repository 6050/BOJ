#include <stdio.h>

int main()
{
    int num;
    scanf("%d", &num);
 
    int i = 0, copy, check, count = 0;
    while ( ++i )
    {
        copy = i;
        check = 0;
        while ( copy )
        {
            if ( copy % 1000 == 666 )
                check = 1;
            copy /= 10;
        }

        if ( check )
        {
            count++;
            if ( count == num ) break;
        }
    }

    printf("%d\n", i);
    return 0;
}
