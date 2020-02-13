import random

def create_network(file_name):
    '''(str)->list of tuples where each tuple has 2 elements the first is int and the second is list of int

    Precondition: file_name has data on social netowrk. In particular:
    The first line in the file contains the number of users in the social network
    Each line that follows has two numbers. The first is a user ID (int) in the social network,
    the second is the ID of his/her friend.
    The friendship is only listed once with the user ID always being smaller than friend ID.
    For example, if 7 and 50 are friends there is a line in the file with 7 50 entry, but there is line 50 7.
    There is no user without a friend
    Users sorted by ID, friends of each user are sorted by ID
    Returns the 2D list representing the frendship nework as described above
    where the network is sorted by the ID and each list of int (in a tuple) is sorted (i.e. each list of friens is sorted).
    '''
    friends = open(file_name).read().splitlines()

    for i in range(len(friends)):
        friends[i] = friends[i].split( )
    
    users = usersInTheNetwork(file_name)
    
    network = list(range(len(users)))
    
    num_users = int(friends[0][0])

    network = list(range(10))
    
    for i in range(num_users):

        userfriends = []

        for n in range(len(friends)-1):
            n += 1                   
            if users[i] == int(friends[n][0]):
                userfriends.append(int(friends[n][1]))

        for n in range(len(friends)-1):
            n += 1
            if users[i] == int(friends[n][1]):
                userfriends.append(int(friends[n][0]))

        userfriends = set(userfriends)
        userfriends = sorted(userfriends)

        tup = (users[i], userfriends)

        network[i] = tup   
    
    return network

def usersInTheNetwork(filename):
    '''str -> lst
    function returns list of sorted users in the network.
    '''

    friends = open(file_name).read().splitlines()

    for i in range(len(friends)):
        friends[i] = friends[i].split( )
        
    users = []
    
    num_users = int(friends[0][0])
    
    for i in range(len(friends)-1):
        i += 1
        if int(friends[i][0]) not in users:
            users.append(friends[i][0])

    for i in range(len(friends)-1):
        i += 1
        if int(friends[i][1]) not in users:
            users.append(friends[i][1])

    

    for i in range(len(users)):
        users[i] = int(users[i])

    users = set(users)
    users = sorted(users)

    return users

def getCommonFriends(user1, user2, network):
    '''(int, int, 2D list) ->int
    Precondition: user1 and user2 IDs in the network. 2D list sorted by the IDs, 
    and friends of user 1 and user 2 sorted 
    Given a 2D-list for friendship network, returns the sorted list of common friends of user1 and user2
    '''
    common=[]

    for i in range(len(network)):
        if user1 == network[i][0]:
            user1_friends = network[i][1]

    for i in range(len(network)):
        if user2 == network[i][0]:
            user2_friends = network[i][1]

    if len(user1_friends) >= len(user2_friends):
        length = len(user1_friends)

        for i in range(length):
            if user1_friends[i] in user2_friends:
                common.append(user1_friends[i])

    else:
        length = len(user2_friends)

        for i in range(length):
            if user2_friends[i] in user1_friends:
                common.append(user2_friends[i])

    common = sorted(common)

    return common

    
def recommend(user, network):
    '''(int, 2Dlist)->int or None
    Given a 2D-list for friendship network, returns None if there is no other person
    who has at least one neighbour in common with the given user and who the user does
    not know already.
    
    Otherwise it returns the ID of the recommended friend. A recommended friend is a person
    you are not already friends with and with whom you have the most friends in common in the whole network.
    If there is more than one person with whom you have the maximum number of friends in common
    return the one with the smallest ID. '''

    '''
    users = []
    usersfriends = network[user][1]
    usersnotfriends = []
    numofcommon = 0
    recomended = 0
    
    
    for i in range(len(network)):
        users.append(int(network[i][0]))

    numusers = len(users)

    for i in range(len(usersfriends)):
        usersnotfriends = users.remove(usersfriends[i])
        usersnotfriends = users.remove(user)

    for i in range(len(users)):
        common = len(getCommonFriends(user, users[i], network))
                   
        if common > numofcommon:
            numofcommon = common
            recomended = users[i]
            
    if numofcommon == 0:
        return None

    if len(usersfriends) == (numusers-1):
        return None

    if len(usersfriends) == 0:
        return None
    
    else:
        return recomended
    '''

    return None
        
    

def k_or_more_friends(network, k):
    '''(2Dlist,int)->int
    Given a 2D-list for friendship network and non-negative integer k,
    returns the number of users who have at least k friends in the network
    Precondition: k is non-negative'''

    userswithKfriends = []

    for i in range(len(network)):
        if len(network[i][1]) >= k:
           userswithKfriends.append(network[i][0])

    return len(userswithKfriends)
            
def maximum_num_friends(network):
    '''(2Dlist)->int
    Given a 2D-list for friendship network,
    returns the maximum number of friends any user in the network has.
    '''
    maxfriends = 0
    for i in range(len(network)):
        if len(network[i][1]) > maxfriends:
            maxfriends = len(network[i][1])

    return maxfriends
        
    
def people_with_most_friends(network):
    '''(2Dlist)->1D list
    Given a 2D-list for friendship network, returns a list of people (IDs) who have the most friends in network.'''

    maxfriends = maximum_num_friends(network)
    
    max_friends=[]

    for i in range(len(network)):
        if len(network[i][1]) == maxfriends:
            max_friends.append(network[i][0])
    
    return max_friends


def average_num_friends(network):
    '''(2Dlist)->number
    Returns an average number of friends overs all users in the network'''

    averagefriendsum = 0

    for i in range(len(network)):
        averagefriendsum = averagefriendsum + len(network[i][1])

    averagefriends = averagefriendsum / len(network)

    return averagefriends
    

def knows_everyone(network):
    '''(2Dlist)->bool
    Given a 2D-list for friendship network,
    returns True if there is a user in the network who knows everyone
    and False otherwise'''
    
    for i in range(len(network)):
        if len(network[i][1]) == (len(network) - 1):
               return True

    return False 


####### CHATTING WITH USER CODE:

def is_valid_file_name():
    '''None->str or None'''
    file_name = None
    try:
        file_name=input("Enter the name of the file: ").strip()
        f=open(file_name)
        f.close()
    except FileNotFoundError:
        print("There is no file with that name. Try again.")
        file_name=None
    return file_name 

def get_file_name():
    '''()->str
    Keeps on asking for a file name that exists in the current folder,
    until it succeeds in getting a valid file name.
    Once it succeeds, it returns a string containing that file name'''
    file_name=None
    while file_name==None:
        file_name=is_valid_file_name()
    return file_name


def get_uid():
    '''()->int
    Keeps on asking for a user ID that exists in the network
    until it succeeds. Then it returns it'''

    usersnet = usersInTheNetwork(file_name)

    ID = None

    while ID == None:
        try:
            ID = int(input("Enter an integer for a user ID:  "))
            if ID not in usersnet:
                print("That user ID does not exist")
                ID = None

        except ValueError:
            print("That was not an integer. Please try again.")
            ID = None

    return ID




##############################
# main
##############################

# NOTHING FOLLOWING THIS LINE CAN BE REMOVED or MODIFIED

file_name=get_file_name()
    
net=create_network(file_name)

print("\nFirst general statistics about the social network:\n")

print("This social network has", len(net), "people/users.")
print("In this social network the maximum number of friends that any one person has is "+str(maximum_num_friends(net))+".")
print("The average number of friends is "+str(average_num_friends(net))+".")
mf=people_with_most_friends(net)
print("There are", len(mf), "people with "+str(maximum_num_friends(net))+" friends and here are their IDs:", end=" ")
for item in mf:
    print(item, end=" ")

print("\n\nI now pick a number at random.", end=" ")
k=random.randint(0,len(net)//4)
print("\nThat number is: "+str(k)+". Let's see how many people has that many friends.")
print("There is", k_or_more_friends(net,k), "people with", k, "or more friends")

if knows_everyone(net):
    print("\nThere at least one person that knows everyone.")
else:
    print("\nThere is nobody that knows everyone.")

print("\nWe are now ready to recommend a friend for a user you specify.")
uid=get_uid()
rec=recommend(uid, net)
if rec==None:
    print("We have nobody to recommend for user with ID", uid, "since he/she is dominating in their connected component")
else:
    print("For user with ID", uid,"we recommed the user with ID",rec)
    print("That is because users", uid, "and",rec, "have", len(getCommonFriends(uid,rec,net)), "common friends and")
    print("user", uid, "does not have more common friends with anyone else.")
        

print("\nFinaly, you showed interest in knowing common friends of some pairs of users.")
print("About 1st user ...")
uid1=get_uid()
print("About 2st user ...")
uid2=get_uid()
print("Here is the list of common friends of", uid1, "and", uid2)
common=getCommonFriends(uid1,uid2,net)
for item in common:
    print(item, end=" ")

    
