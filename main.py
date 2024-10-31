from Request import *

usernames = [None, "", "colin", "colin lambert"]
emails = [None, "", "colin@gmail.com", "colin lambert@yahoo.com"]
totalVolumes = [None, None, None, None]
totalWeights = [None, None, None, None]
totalCosts = [None, None, 5, None]

users = [User(usernames[i], emails[i], totalVolumes[i], totalWeights[i], totalCosts[i]) for i in range(len(usernames))]
# for i in range(len(usernames)) : print(users[i])

volumes = [None, None, None, 2]
weights = [None, 3, None, 10.23]
costs = [None, None, 5.1, 293.2]

orders = [Order(volumes[i], weights[i], costs[i]) for i in range(len(volumes))]
for i in range(len(volumes)) : print(orders[i])