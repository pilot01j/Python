class User:
    #constructor
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #metoda din constructor
    def follow(self, user):
        user.followers += 1
        self.following += 1

#crearea unui obiect pe baza constructorului
user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)

print(user_1.followers)