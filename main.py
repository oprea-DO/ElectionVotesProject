members = 70
validBallots = 64
seats = 2
votes = []

quota = (validBallots / (seats+1) + 1)
f = open("Test1_Votes.txt")

for i in range(0, 63):
  line = f.readline()
  line = line.split(",")
  line = [int(x) for x in line]
  votes.append(line)
print(votes)
