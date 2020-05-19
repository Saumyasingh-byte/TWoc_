from collections import Counter
n=int(input("Enter the total no. of votes casted: "))
votes=[]
for i in range (n):
    votes[i]=input("Enter the candidate's name: ")
vote_count=Counter(votes)
max_votes=max(vote_count.values())
lst=[i for i in vote_count.keys() if vote_count[i]==max_votes] 
print(sorted(lst)[0]) 
