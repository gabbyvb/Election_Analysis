# Retrieve data
import csv
import os

file_to_load = os.path.join("election_results.csv")
file_to_save = os.path.join("../Analysis", "election_analysis.txt")

with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    headers = next(file_reader)
    print(headers)

# Calculate total # of votes cast
# List of candidates who received votes
# Perecentage of votes each candidate won
# Total # of votes each candidate won
# Winner of election based on popular vote
# Write results to file

with open(file_to_save, "w") as txt_file:
    txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")