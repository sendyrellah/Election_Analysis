# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number fo votes each candidate won
# 5. The winner of the election bases on popular vote.

# Add our dependencies.

import csv

import os

# Assign a variable to load a file from a path.

file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.

file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
# outfile.write("Hello World")

#Write three counties to the file.
outfile.write("Counties in the Election\n---------------------\nAraphahoe\nDenver\nJefferson")

# Close the file
outfile.close()














