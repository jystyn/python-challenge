import csv
import os

#relative path to data file Python_Starter/python-challenge/PyPoll/Resources/election_data.csv
election_data_csv = os.path.join("Python_Starter","python-challenge","Pypoll", "Resources", "election_data.csv")

#create list to store data
election_data = []
candidate_list = []


with open(election_data_csv) as csvfile:
    reader=csv.DictReader(csvfile)

    for row in reader:
        election_data.append({"Voter ID": int(row["Ballot ID"]), "County": row["County"], "Candidate": row["Candidate"]})

#print(election_data)
        
total_votes = len(election_data)
total_candidates = len(candidate_list)
# print(total_votes)
#cand_votes = candidate_list[0]["Votes"]
for i in range(total_votes):
    if election_data[i]["Candidate"] not in candidate_list:
        candidate_list.append({"Candidate": election_data[i]["Candidate"], "Votes": 1})
    # else:
    #     for x in range(total_candidates):
    #         if candidate_list[x]["Candidate"].value() == election_data[i]["Candidate"].value():
    #             candidate_list[x]["Votes"] = candidate_list[x]["Votes"] + 1

        
print(candidate_list)

    

#total votes each candidate won
       

#percentage of votes won
        

#winner based upon popular vote        

# txt_output = (
#     f'Election Analysis\n'
#     f'----------------------------\n'
#     f'Total Months: {candidate_list}\n'
#     #f'Total: ${net_total}\n'
#     #f'Average Change: ${average}\n'
#     #f'Greastest Increase in Profits: {max_increase["Month"]} ${max_increase["Change"]}\n'
#     #f'Greastest Decrease in Profits: {max_decrease["Month"]} ${max_decrease["Change"]}\n'
# ) 

# print(txt_output)

# new_file = "python-challenge/PyPoll/Analysis/result.txt"

# with open(new_file, "w") as f:
#     f.write(txt_output)