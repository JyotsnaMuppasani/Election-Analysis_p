#The data we need to retrieve
import csv
import os
#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Candidate options and candidate votes
candidate_options = []  
candidate_votes = {}

#Open the election results and read the file
with open(file_to_load) as election_data:

    file_reader = csv.reader(election_data)

#Read the header row.
    headers = next(file_reader)
#Print each row in the CSV file.

    for row in file_reader:
        #add to total vote count
        total_votes += 1
        #print the candidate name fron each row
        candidate_name = row[2]
          
        #if candidate name does not match any existing candidate
        if candidate_name not in candidate_options:
            
             #add the candidate name to the candidate list
             candidate_options.append(candidate_name)
             #begin tracking that candidates votes count
             candidate_votes[candidate_name] = 0
  
        #add votes to that candidates count
        candidate_votes[candidate_name] += 1

#Iterate through the candidate list
for candidate_name in candidate_votes:
     #retreive vote count of a candidate
     votes = candidate_votes[candidate_name]
     #calculate percentage of votes
     vote_percentage = float(votes) / float(total_votes)*100
     #print the candidate name and percentage of votes
     #print(f"{candidate_name}; received {vote_percentage:.1f}% of the vote.")
    
    
     #determine if the votes are greater than winning count
     if (votes > winning_count) and (vote_percentage>winning_percentage):
         winning_count = votes
         winning_percentage = vote_percentage
         winning_candidate = candidate_name
     print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")


winning_candidate_summary = (
    f"-------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote count: {winning_count}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------\n")
print(winning_candidate_summary)







