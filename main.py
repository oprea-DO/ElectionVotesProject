members = 70
validBallots = 64
seats = 2
votes = []

quota = (validBallots / (seats+1) + 1)

f = open("Test1_Votes.txt")
line = f.read()
votes = line.split()
print(votes)
