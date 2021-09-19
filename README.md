# Election_Analysis

## Overview of Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate total number of votes cast
2. Get a complete list of candidates who received votes
3. Calculate the total number of votes each candidate received
4. Calculate the percentage of votes each candidate won
5. Determine the winner of the election based on the popular vote

## Resources
- Data source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code: 1.38.1

## Election-Audit Results
The analysis of the election show that:
- There were 369,711 votes cast.
- Breakdown of County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)
- Denver County had the largest number of votes.
- Breakdown of Candidate Votes:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
- Election Results:
    Winner: Diana DeGette
    Winning Vote Count: 272,892
    Winning Percentage: 73.8%

## Election-Audit Summary
In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.

To modify this script to be used for any election, the 'file_to_load' variable should be updated to the appropriate csv file that contains the election results.

````python
file_to_load = os.path.join("election_results.csv")
````

Next, depending on the format of the election results file, it may be necessary to update the column reference to ensure the apprpriate column is referenced for candidate name & county.

````python
# Get the candidate name from each row.
  candidate_name = row[2]

# Extract the county name from each row.
  county_name = row[1]
 ````
  
