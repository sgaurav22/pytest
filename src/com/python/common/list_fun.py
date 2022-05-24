lucky_number = [4,8,15,16,23,42]
friends = ["micky", "vicky", "tikki", "money", "sunny"]
#friends.extend(lucky_number)
#friends.append("ricky")
#friends.insert(1,"ricky")
#friends.sort()
#friends.remove("money")
#friends.clear()
#friends.pop()  # remove last element of list

# reverse and copy functions
friends.reverse()
friends_copy = friends.copy()
print(friends_copy)

#friends.append("micky")
#print(friends.count("micky"))

# check if value exist if it does return its index else throw exception
#print(friends.index("money"))