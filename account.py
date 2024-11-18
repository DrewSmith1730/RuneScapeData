# basic class to store basic important data pertaining to each individual account I have


# Accout Class
# Used to differentiate my different RuneScape Accounts

# User -> String: Account Username
# Type -> String: Account Type ie: (Main, IronMan, HCIronMan, etc) [Maybe swap to integer using a dictionary idk yet]
# skilltotal -> Int: skill total : defualt 0
# xptotal -> Int: Xp total : default 0
# skills -> Int Array : for all skill levels
# xp -> Int Array : xp totals for each individual skill
# 


class Account:
    def __init__(self, user, type, skilltotal, xptotal, skills, xp):
        self.user = user
        self.type = "Main"
        self.skilltotal = skilltotal
        self.xptotal = 0
        self.skills = []
        self.xp = 0

    def get_user(self):
        return self.user

    def set_user(self, value):
        self.user = value

    def get_type(self):
        return self.type

    def set_type(self, value):
        self.type = value

    def get_skilltotal(self):
        return self.skilltotal

    def set_skilltotal(self, value):
        self.skilltotal = value

    def get_xptotal(self):
        return self.xptotal

    def set_xptotal(self, value):
        self.xptotal = value

    def get_skills(self):
        return self.skills

    def set_skills(self, value):
        self.skills = value

    def get_xp(self):
        return self.xp

    def set_xp(self, value):
        self.xp = value



