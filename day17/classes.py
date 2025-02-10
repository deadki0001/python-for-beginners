class User:
          ### Init is the Construnctor
    def __init__(self, user_id, username): # self is the object being initialized
        #initialize attributes
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0 

# Method
    def follow(self, user):
        user.followers += 1
        self.following += 1
        

user_1 = User("001", "devon")   # Init will be called
user_2 = User("002", "parkboyoung")    # Init will be called

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

# Constructor
# Also known as initializing. You can set variables or counters to their starting values.