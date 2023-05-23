"""
TUTORIAL FILE.
The Quiz Program is in my-quiz-project(OOP) and quiz-project-angela.py
"""


class User:
    def __init__(self):
        print("New user is being created")


user1 = User()
user1.id = "001"
user1.username = "opeyemi"
print(user1.username)

user2 = User()
user1.id = "002"
user1.username = "jack-bauer"
print(user1.username)
####################################

# CONSTRUCTORS
"""
Suppose we wanted to have the same variables (perhaps a lot of them) various objects in a class
We can use constructors to specify what should happen when our object is being constructed. 
This is also known as 'initialize' an object. And it is done by way of a special function.
the '__init__' function
"""


class User_:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0  # Default value for all object. Does not need to be passed when object is created.
                            # It already has a default value zero which will be in all objects created.
                            # Look below for my fooling around.
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User_('001', 'angela')
user_2 = User_('002', 'Jack Bauer')

print(f"User1 followers before follow: {user_1.followers}\nUser1 following before follow: {user_1.following}")
print(f" User2 followers before follow: {user_2.followers}\n User2 following before follow: {user_2.following}")
user_1.follow(user_2)
user_2.follow(user_1)
print(f"User1 followers after follow: {user_1.followers}\nUser1 following after follow: {user_1.following}")
print(f" User2 followers after follow: {user_2.followers}\n User2 following after follow: {user_2.following}")


######################################
user_name = input("What's your username? ")

user0000000015 = User_('001', user_name)
print(user0000000015.followers)
print(user0000000015.username)

# Fooling around with a sort of followers tracker
app_is_on = True
while app_is_on:
    follow = input("Do you want to follow User0000000015? (y/n)").lower()
    if follow == 'y':
        user0000000015.followers += 1
        print(f"User0000000015 has {user0000000015.followers} followers.")
    else:
        print(f"User0000000015 final:: {user0000000015.followers} followers.")
        app_is_on = False
