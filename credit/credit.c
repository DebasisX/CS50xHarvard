#include <cs50.h>
#include <stdio.h>
int checkSum(long f) // To check if no. is a valid credit card
{
    long j = f;

    int b = 1;
    int d;
    int y = 0;
    int m = j % 10;
    do
    {
        j = j / 10;
        d = j % 10;
        b += 1;
        if (b % 2 == 0)
        {
            if ((d * 2) >= 10)
            {
                y = y + ((d * 2) / 10) + ((d * 2) % 10);
                continue;
            }
            if ((d * 2) <= 10)
            {
                y = y + (d * 2);
                continue;
            }
        }
        else
        {
            m = m + d;
            continue;
        }
    }
    while (j != 0);
    int z = y + m;
    if ((z % 10) == 0)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int main(void)
{
    int b = 1;
    long c = get_long("Number:");
    int a = 0;
    long n = c;
    long first = c;
    long sec = c;
    long f = c;
    do
    {
        n = n / 10;
        a += 1;
    }
    while (n != 0);
    int x = checkSum(f);

    /*
    American Express Digits : 15    Starts with : 34 or 37
    MasterCard Digits : 16   Starts with : 51 to 55
    VISA : 13 or 16   Starts with : 4
    */
    while (first >= 10)
    {
        first = first / 10;
    }
    while (sec >= 100)
    {
        sec = sec / 10;
    }
    if ((x == 1) && (a == 15) && (first == 3) && ((sec == 34) || (sec == 37))) //checking for American Express
    {
        printf("AMEX\n");
    }
    else if ((x == 1) && (a == 16) && (first == 5) && ((sec == 51) || (sec == 52) || (sec == 53) || (sec == 54) || (sec == 55)))
    {
        printf("MASTERCARD\n"); //checking for MasterCard
    }
    else if ((x == 1) && ((a == 13) || (a == 16)) && (first == 4)) //checking for VISA
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n"); //else INVALID
    }
}


