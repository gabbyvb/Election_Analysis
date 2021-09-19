# Retrieve data
import csv
import os

file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join("../Analysis", "election_analysis.txt")

total_votes = 0
# List of candidates
candidate_options = []
# Dictionary to match candidates with vote count
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Skip header row in file reader
    headers = next(file_reader)
   
    for row in file_reader:
        # Calculate total # of votes cast
        total_votes += 1

        # List of candidates who received votes
        candidate_name = row[2]

        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

             # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    with open(file_to_save, "w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"------------------------\n")
        print(election_results, end="")
        # Write results to file
        txt_file.write(election_results)

        for candidate_name in candidate_votes: # Iterate through the candidate list
            votes = candidate_votes[candidate_name] # Retrieve vote count of a candidate

            # Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print the candidate name and percentage of votes.
            #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            # Winner of election based on popular vote
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate_name

            winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        txt_file.write(winning_candidate_summary)