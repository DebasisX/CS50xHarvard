// Implements a dictionary's functionality

#include <ctype.h>
#include <stdio.h>
#include <stdbool.h>
#include <strings.h>
#include <string.h>
#include "dictionary.h"
#include <stdlib.h>
#include <ctype.h>

int count = 0;
unsigned int size(void);

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 10000;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO is DONE!
    int hash_index = hash(word);

    node *temp = table[hash_index];
    while (temp != NULL)
    {
        if (strcasecmp(word, temp->word) == 0)
        {
            return true;
        }
        else
        {
            temp = temp->next;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int length_string = strlen(word);
    int hashed = 0;
    for (int i = 0; i < length_string - 1; i++)
    {
        hashed += (4 * i);
    }
    if (hashed > N)
    {
        hashed = hashed % N;
    }

    // TODO: Improved!
    return hashed;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO is DONE!
    FILE *f = fopen(dictionary, "r");
    char text[LENGTH + 1];
    if (f == NULL)
    {
        printf("Could not Load Dictionary...");
        return false;
    }
    else if (f != NULL)
    {
        while (fscanf(f, "%s", text) != EOF)
        {
            node *temp = malloc(sizeof(node));
            if (temp == NULL)
            {
                return false;
            }
            else if (temp != NULL)
            {
                strcpy(temp->word, text);
                temp->next = NULL;

                int hash_index = hash(text);
                if (table[hash_index] == NULL)
                {
                    table[hash_index] = temp;
                }
                else if (table[hash_index] != NULL)
                {
                    temp->next = table[hash_index];
                    table[hash_index] = temp;
                }
                count++;
            }
        }
        fclose(f);
        return true;
    }
    else
    {
        return false;
    }
}
// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO is DONE!
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++)
    {
        node *temp1 = table[i];
        node *temp2 = table[i];
        while (temp2 != NULL)
        {
            temp1 = temp1->next;
            free(temp2);
            temp2 = temp1;
        }
    }
    // TODO is DONE
    return true;
}
