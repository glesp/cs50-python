import csv
import sys


def main():

    # TODO: Check for command-line usage
    if not len(sys.argv) == 3:
        print("Usage: .csv file then .txt file ie. the test sequence")

    # TODO: Read database file into a variable
    rows = []

    with open(f"{sys.argv[1]}") as file:
        reader = csv.DictReader(file)
        for row in reader:
            rows.append(row)


    # TODO: Read DNA sequence file into a variable

    with open (f"{sys.argv[2]}") as file2:
        lines = file2.read()

    # TODO: Find longest match of each STR in DNA sequence
    match_list = []
    match_dict = dict()
    for i in range(1, len(reader.fieldnames)):
        longest_match_variable = longest_match(lines, reader.fieldnames[i])
        match_dict[reader.fieldnames[i]] = str(longest_match_variable)




    # TODO: Check database for matching profiles
     #create copy of dictionary but remove name key for comparison to new dict
    for row in rows:
        row_copy = row.copy()
        row_copy.pop('name', None)
        if row_copy == match_dict:
            print(row['name'])
            break
    else:
        print("No match")
    



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
