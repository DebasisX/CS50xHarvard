#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

#include "wav.h"

int check_format(WAVHEADER header);
int get_block_size(WAVHEADER header);

int main(int argc, char *argv[])
{
    // Ensure proper usage
    // TODO #1
    if (argc != 3)
    {
        printf("Usage : ./reverse input.wav output.wav");
        return 1;
    }

    // Open input file for reading
    // TODO #2
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Invalid Input");
        return 1;
    }

    // Read header
    // TODO #3
    WAVHEADER header;
    fread(&header, sizeof(WAVHEADER), 1, input);

    // Use check_format to ensure WAV format
    // TODO #4
    int n = 0;
    n = check_format(header);
    if (n != 0)
    {
        return 1;
    }

    // Open output file for writing
    // TODO #5
    FILE *output = fopen(argv[2], "w");

    // Write header to file
    // TODO #6
    fseek(input, 0, SEEK_SET);
    fwrite(&header, sizeof(WAVHEADER), 1, output);

    // Use get_block_size to calculate size of block
    // TODO #7
    int bs = get_block_size(header);
    char buffer[bs];

    // Write reversed audio to file
    // TODO #8
    fseek(input, -bs, SEEK_END);
    while (ftell(input) >= (sizeof(WAVHEADER)))
    {
        fread(&buffer, bs, 1, input);
        fwrite(&buffer, bs, 1, output);
        fseek(input, -2 * bs, SEEK_CUR);
    }

    fclose(output);
    fclose(input);
}
int check_format(WAVHEADER header)
{
    // TODO #4
    if (header.format[0] != 'W')
    {
        return 1;
    }
    else if (header.format[1] != 'A')
    {
        return 1;
    }
    else if (header.format[2] != 'V')
    {
        return 1;
    }
    else if (header.format[3] != 'E')
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
int get_block_size(WAVHEADER header)
{
    // TODO #7
    int blocksize = header.numChannels * (header.bitsPerSample / 8);
    return blocksize;
}