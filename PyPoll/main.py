import os
filepath = os.path.join ("data","election_data.csv")

file_object = open ("Results.txt", "w" )
#total number votes cast
filename = "election_data.csv"
header_key = "Voter ID"

voter = []
county =[]
candidate = []
candidate_dict = {}
with open (filename) as f:
    for line in f:
        (v, c, ca) = line.rstrip().split(',')
#ignoring top line
        if header_key not in v:      
            voter.append (v)
            county.append (c)
            candidate.append (ca)
            total_votes = (len(voter))
            candidate_dict[ca] = candidate_dict.get(ca, 0) + 1

output = "Election Results\n" 
output = output + "-------------------------\n"
output = output + "Total Votes: " + str(total_votes) + "\n"
output = output + "--------------------------\n"
for key in candidate_dict.keys ():
    votes = candidate_dict[key]
    vote_pct = ((votes / total_votes) * 100)
    output = output + (f'{key}: {vote_pct:.3f}% ({votes})') + "\n"
output = output + "---------------------------\n"

winner = max (candidate_dict, key=candidate_dict.get)
output = output + "Winner: " + winner + "\n"
file_object.write(output)
print (output)



