#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>


int main(int argc, string argv[])
{
    int i, j;
    int c = 0;

    string str = argv[1];
    if (argc != 2) //checking if there is more or less than 1 argument passed
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    int length = strlen(str) - 1;
    for (i = 0; i <= length; i++)
    {
        c++;
        int a = 0;
        str[i] = tolower(str[i]);
        int ch = (int)str[i];
        if (ch < 97 || ch > 122) //if key contains  characters other than alphabets exit(0)
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
        else
        {
            for (j = 0; j <= length; j++) //checking using linear search if there are same characters repeated in key
            {
                string str1 = argv[1];
                str1[j] = tolower(str[j]);
                int ch1 = (int)str1[j];
                if (ch1 == ch)
                {
                    ++a;
                    if (a > 1)
                    {

                        printf("same letters cannot be repeated");
                        return 1;
                    }
                }
            }
        }
    }

    if (c != 26)//checking for 26 letters only
    {
        printf("Key must contain 26 characters.");
        return 1;
    }

    string str2 = get_string("plaintext:");
    int length1 = strlen(str2);
    char final[length1];
    for (int m = 0; m <= length1; m++)
    {
        char h = str2[m];
        if (isalpha(h))
        {
            int y = h;
            if (isupper(str2[m]))
            {
                int diff = y - 65; //substracting y from A to find position in argv
                char st = str[diff];
                final[m] = toupper(st); //converting to respective cases and assigning to final
                continue;
            }
            else
            {
                int diff = y - 97; //substracting y from A to find position in argv
                char st = str[diff];
                final[m] = tolower(st); //converting to respective cases and assigning to final
                continue;
            }
        }
        else
        {
            final[m] = str2[m]; //assigning to final non alphabetical characters
            continue;
        }
    }
    printf("ciphertext: %s\n", final);
    return 0;

}
