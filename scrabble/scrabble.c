#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>
// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);
int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");
    int len1 = strlen(word1) - 1;
    int len2 = strlen(word2) - 1;

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);




    // TODO: Print the winner
    if (score1 > score2)
    {
        printf("Player 1 Wins !%i\n");
    }
    else if (score2 > score1)
    {
        printf("Player 2 Wins !\n");
    }
    else
    {
        printf("Tie\n");
    }
}


int compute_score(string word)
{
    // TODO: Compute and return score for string
    int i;
    int a = 0;
    for (i = 0; i <= (strlen(word) - 1); i++)
    {
        char c = tolower(word[i]); //converting to lowercase
        char d = 'a';

        int diff = (int)c - (int)d;
        if (diff < 0 || diff > 25) //checking and eiminating other characters except lowercases
        {
            continue;
        }
        else
        {


            a = a + (int)POINTS[diff]; //adding all the values of alphabets from POINTS
            continue;
        }


    }


    return a;
}