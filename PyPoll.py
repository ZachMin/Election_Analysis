# Add dependencies
import csv
import os

# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save te file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a vote counter
total_votes = 0

# Candidate options and candidate votes
candidate_options = []
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

with open(file_to_save, "w") as txt_file:
# Print final vote count to the terminal
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    # Save final vote count to the text file
    txt_file.write(election_results)


    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100

        # To do: print out each candidates name, vote count and percentage of votes to the terminal

        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)

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
    # Save the winning candidates name to the text file
    txt_file.write(winning_candidate_summary)
