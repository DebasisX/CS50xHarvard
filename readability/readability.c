#include <cs50.h>
#include <string.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

int grade(string str);
int main(void)
{
    //taking string input
    string str = get_string("Text: ");
    int g;
    g = grade(str); //sending to function
    //returning output accordingly
    if (g >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (g < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %i\n", g);
    }
}
int grade(string str)
{
    int length = strlen(str);
    length = length - 1;
    double l, w, s;
    s = 0.0;
    w = 1.0;
    l = 0.0;
    int i;
    for (i = 0; i <= length; i++)
    {
        char ch = tolower(str[i]); //converting all letters to lowercase
        int a = (int)ch;

        if ((a >= 97) && (a <= 122)) //counting all letters
        {
            ++l;
        }
        else if (a == 32) //checking for words by counting spaces
        {
            w++;
        }
        else if (a == 33 || a == 46 || a == 63) //checking for periods to count sentences
        {
            s++;
        }
        else
        {
            continue;
        }
    }

    double L = (l / w) * 100;
    double S = (s / w) * 100;
    double index = round((0.0588 * L) - (0.296 * S) - 15.8); //putting all values n the formula to estimate grade
    int grade = index;
    return grade; //returning the grade
}