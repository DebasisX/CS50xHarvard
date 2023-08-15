#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;
    int i = 1;
    do
    {
        h = get_int("Height:"); //taking the height as input and if wrong inputs are provided then re-prompting user to input right input.
        if ((h > 0) && (h <= 8))
        {
            break;
        }
        else
        {
            continue;
        }
    }
    while (i > 0);
    //printing blocks as per height requirement
    if (h == 1)
    {
        printf("#  #\n");
    }
    if (h == 2)
    {
        printf(" #  #\n");
        printf("##  ##\n");
    }
    if (h == 3)
    {
        printf("  #  #\n");
        printf(" ##  ##\n");
        printf("###  ###\n");
    }
    if (h == 4)
    {
        printf("   #  #\n");
        printf("  ##  ##\n");
        printf(" ###  ###\n");
        printf("####  ####\n");
    }
    if (h == 5)
    {
        printf("    #  #\n");
        printf("   ##  ##\n");
        printf("  ###  ###\n");
        printf(" ####  ####\n");
        printf("#####  #####\n");
    }
    if (h == 6)
    {
        printf("     #  #\n");
        printf("    ##  ##\n");
        printf("   ###  ###\n");
        printf("  ####  ####\n");
        printf(" #####  #####\n");
        printf("######  ######\n");
    }
    if (h == 7)
    {
        printf("      #  #\n");
        printf("     ##  ##\n");
        printf("    ###  ###\n");
        printf("   ####  ####\n");
        printf("  #####  #####\n");
        printf(" ######  ######\n");
        printf("#######  #######\n");
    }
    if (h == 8)
    {
        printf("       #  #\n");
        printf("      ##  ##\n");
        printf("     ###  ###\n");
        printf("    ####  ####\n");
        printf("   #####  #####\n");
        printf("  ######  ######\n");
        printf(" #######  #######\n");
        printf("########  ########\n");
    }
}
