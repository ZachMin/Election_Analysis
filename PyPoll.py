# Add dependencies

import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save te file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a vote counter
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object witht the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    for row in file_reader:
        # Add to the total vote count
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # If the candidate does not match any existing one...
        if candidate_name not in candidate_options:
            # add it to list of candidates
            candidate_options.append(candidate_name)

            # Begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] += 1

# Determine percentage of votes for each candidate by looping through the counnts
# 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    # 2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # 3. Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    # To do: print out each candidates name, vote count and percentage of votes to the terminal

    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    # Determine winning vote count and candidate/ Determine if the votes is greater than the win count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent = Vote percentage
        winning_count = votes
        winning_percentage = vote_percentage
        # Set the winning_canditate equal to their name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"------------------------\n")
print(winning_candidate_summary)

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
