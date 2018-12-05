### PyPoll Script:
### Analyzing election data
### Tomoko Takita
### December 2018

import csv

 # initialize variables

totalVotes = 0

# Open the CSV file in read-only mode

with open("election_data.csv", "r") as data:

    # Parse de CSV file
    reader = csv.reader(data)

    # Read the Header from the Data in order to exclude it from the analysis
    next(data)

    # Loop through the lines/rows in the data
    for row in reader:
    # Count total number of vote cast    
        totalVotes += 1        

    # Put the name of the candidate in a list
    # total number of votes of each candidates
    #Candidates =[]
    #data.seek(0)
    #next(data)
    #for row in reader:
        #if row[2] not in Candidates:
            #Candidates.append(row[2])
    #print(Candidates)
  
    # Put the name of the candidate in a list
    # total number of votes of each candidates
    data.seek(0)
    next(data)
    dic ={}
    for row in reader:
        if str(row[2]) not in dic:
            dic[str(row[2])] = 1
        else:
            dic[str(row[2])] += 1
    #print(dic)

 # the winner of the election
    import operator
    #(print(max(dic.items(),key=operator.itemgetter(1))[0]))
    

# print results in terminal
print("Total Votes:"   + str(totalVotes))
for candidate, votes in dic.items():
        print(f"name: {candidate} {'{:,.3f}'.format((votes/totalVotes)*100)}% ({votes})")
#print(f'"Winner: "{max(dic.items(),key=operator.itemgetter(1))}')
max_winner = max(dic.items(),key=operator.itemgetter(1))
print("Winner: " +max_winner[0])
#(print(max(dic.items(),key=operator.itemgetter(1))[0]))

# Create/fill/Close the Results file
results = open("results_pypoll.txt", "w")
results.write(f"Total Votes:   "+ str(totalVotes)+ "\n")
for candidate, votes in dic.items():
    results.write(f"name: {candidate} {'{:,.3f}'.format((votes/totalVotes)*100)}% ({votes})"+ "\n")
results.write("Winner: " +max_winner[0])
