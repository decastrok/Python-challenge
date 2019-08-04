import os
import csv

# Path to collect data from the Resources folder
election_data = os.path.join('Resources', 'election_data.csv')

candidates= ["Correy", "Khan", "Li", "O''Tooley"]
CorreyVotes = 0
Correyprct = 0
KhanVotes = 0
Khanprct = 0
LIVotes= 0
LIprct = 0
OTVotes=0
OTprct = 0
TotalVotes=0

with open(election_data)  as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    TotalVotes = sum(1 for line in election_data if line.rstrip('\n'))
    CandidatesTotalVotes = 0
    for candidates in csvreader:
        if election_data[2] == "Correy":
            CorreyVotes = +1
        elif election_data[2] == "Khan":
            KhanVotes = +1
        elif election_data[2] == "Li":
            LIVotes = +1
        else:
            OTVotes= +1
              
    #percentvotes = [TotalVotes / CandidatesTotalVotes*100]
    print(f"Total Votes {TotalVotes}")
    print(f"Correy Votes: {CorreyVotes} + {Correyprct}")
    print(f"Khan Votes: {KhanVotes} + {Khanprct}")
    print(f"Li Votes: {LiVotes} + {Liprct}")
    print(f"O'Tooley Votes: {OTVotes} + {OTprct}")

