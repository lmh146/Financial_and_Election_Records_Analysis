import os
import csv


#Refernce File
PyPoll_csv = os.path.join('Resources', 'election_data.csv').replace("\\", "/")


#Variables
Votes = []

Candidates = ["Khan", "Coorey", "Li", "O'Tooley"]

Total_Votes1 = 0
Total_Votes2 = 0
Total_Votes3 = 0
Total_Votes4 = 0
Prct_Votes = []


#Open File
with open(PyPoll_csv, 'r') as pollfile:
    csv_reader = csv.reader(pollfile, delimiter=',')

     #Skip the First Line
    header = next(csv_reader)

    for row in csv_reader:

        #Total Votes
        Votes.append(row[0])

        #Votes per Candidates
        candidate_choice = row[2]

        if candidate_choice == "Khan":
            Total_Votes1 = Total_Votes1 + 1

        elif candidate_choice == "Correy":
            Total_Votes2 = Total_Votes2 + 1

        elif candidate_choice == "Li":
            Total_Votes3 = Total_Votes3 + 1

        else:
            Total_Votes4 = Total_Votes4 + 1

#Candidate's Precent of the Vote
Overall_Votes = len(Votes)

Can1_Percent = '{:.3f}'.format(round(((Total_Votes1/Overall_Votes) * 100), 3))
Can2_Percent = '{:.3f}'.format(round(((Total_Votes2/Overall_Votes) * 100), 3))
Can3_Percent = '{:.3f}'.format(round(((Total_Votes3/Overall_Votes) * 100), 3))
Can4_Percent = '{:.3f}'.format(round(((Total_Votes4/Overall_Votes) * 100), 3))


#Calculate the Winner
if Can1_Percent > Can2_Percent and Can1_Percent > Can3_Percent and Can1_Percent > Can4_Percent:
    Winner = "Khan"
elif Can2_Percent > Can3_Percent and Can2_Percent > Can4_Percent and Can2_Percent > Can1_Percent:
    Winner = "Correy"
elif Can3_Percent > Can4_Percent and Can3_Percent > Can1_Percent and Can3_Percent > Can2_Percent:
    Winner = "Li"
else:
    Winner = "O'Tooley"


#


#Print Statements
print("Election Results")
print("---------------------------")
print(f'Total Votes: {len(Votes)}')
print("---------------------------")
print(f"Khan: {Can1_Percent}% ({Total_Votes1})")
print(f"Correy: {Can2_Percent}% ({Total_Votes2})")
print(f"Li: {Can3_Percent}% ({Total_Votes3})")
print(f"O'Tooley: {Can4_Percent}% ({Total_Votes4})")
print("---------------------------")
print(f"Winner: {Winner}")

#Write into File
output_pollfile = os.path.join("pollfile.csv")
with open(output_pollfile, 'w') as final_pollfile:
    writer = csv.writer(final_pollfile)

    writer.writerow(["Election Results"])
    writer.writerow(["---------------------------"])
    writer.writerow([f'Total Votes: {len(Votes)}'])
    writer.writerow(["---------------------------"])
    writer.writerow([f"Khan: {Can1_Percent}% ({Total_Votes1})"])
    writer.writerow([f"Correy: {Can2_Percent}% ({Total_Votes2})"])
    writer.writerow([f"Li: {Can3_Percent}% ({Total_Votes3})"])
    writer.writerow([f"O'Tooley: {Can4_Percent}% ({Total_Votes4})"])
    writer.writerow(["---------------------------"])
    writer.writerow([f"Winner: {Winner}"])


