import sys
import csv
# forensic experiment: DNA profiling
# CODIS: Combined DNA Index System
# row = Individual, column = one STR
# Example:
# name,AGAT,AATG,TATC
# Alice,28,42,14
# Bob,17,22,19
# Charlie,36,18,25


def main():
    # STR = Standard Tandem Repeats (short sequences of DNA bases)
    # TODO: Check for command-line usage
    if (len(sys.argv) != 3):
        print("Usage: python dna.py databases.. .db sequences.. .txt")
        quit()
    # TODO: Read database file into a variable
    with open(sys.argv[1], newline='') as csvfile:
        read = csv.reader(csvfile, delimiter=' ', quotechar='|')
        dbsequence = []

        for row in read:
            dbsequence += row

    # TODO: Read DNA sequence file into a variable
    fileopened = open(sys.argv[2], "r")
    sequence = fileopened.read()

    # Finding Substrings

    lst = ""
    listseq = []

    for row in dbsequence:

        lst = row.split()
        listseq += lst
        # print(lst)
        break
    substring = listseq[0]
    # print(substring)
    listnew = substring.split(',')
    listnew.pop(0)
    subseq = ""
    matches = []
    # print(listnew)
    # listnew contains the subsequences to compare against
    # TODO: Find longest match of each STR in DNA sequence
    for i in listnew:
        subseq = i
        match = longest_match(sequence, subseq)
        matches.append(match)
    # print(matches)
    c = 0
    for row in dbsequence:
        c += 1
    c = c - 1

    # matches list has the longest lengths of matches
    # TODO: Check database for matching profiles

    # comparing matches against the values of the databases
    i = 0
    j = 0
    temp = ""
    lst2 = ""
    listsq = []
    everyonesdna = []
    listemp = []

    for row in dbsequence:
        if i == 0:
            i = 1
            continue
        else:
            lst2 = row.split()
            temp = lst2[j]
            listsq = temp.split(',')
            listemp += listsq
            listsq.pop(0)
            everyonesdna += listsq

    dna = []
    dna = [eval(n) for n in everyonesdna]  # converting to integer list
    # print(dna)
    # print(listemp)

    found = True
    found = check_sequence(matches, dna)
    # print(found)
    if found != True:
        print("No match")
        exit()

    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        data = [row[1:] for row in reader]

    # print(data)

    with open(sys.argv[1], newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        names = [row['name'] for row in reader]
    # print(names)
    for x in range(c):
        templist = data[x]
        templist = [eval(n) for n in templist]
        var = check_sequence(matches, templist)
        # print(var)
        if var == True:
            print(names[x])
            break
    return


def check_sequence(lst1, lst2):
    n = len(lst1)
    for i in range(len(lst2) - n + 1):  # checking for the repetition of the integers in a sequence
        if lst2[i: i + n] == lst1:
            return True
    return False


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""
    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)
    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):
        # Initialize count of consecutive runs
        count = 0
        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:
            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length
            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            # If there is no match in the substring
            else:
                break
        # Update most consecutive matches found
        longest_run = max(longest_run, count)
    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()