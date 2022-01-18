# Add dependencies

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save te file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object witht the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement to open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write the three counties to the file.
    txt_file.write("Counties in the Election\n-------------------\nArapahoe\nDenver\nJefferson")

# Close the file

# Using the open() function with the "w" mode we will write data to the file
open(file_to_save, "w")

# Close the file.
election_data.close()










# 1. Total number of votes cast
# 2. Complete list of candidates that received votes
# 3. Percentage of votes each candidate won
# 4. Total number of votes each candidate won
# 5. Winner of election based on popular vote
