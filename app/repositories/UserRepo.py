import json
from app.utils.UserUtil import UserUtil
from app.models.User import User
from .__init__ import *


class UserRepo(BaseRepo):

    def __init__(self, collection: str="users") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_user(self, user: User):
        res = self.collection.insert_one(user.__dict__)
        return res

    def get_token_by_email(self, email):
        users = list(self.collection.find({"email": email}))
        count = 0
        for record in users:
            count += 1
        if count < 1:
            return None
        else:
            return UserUtil.format_token(users[0])
        
    def get_user_by_email(self, email):
        users = list(self.collection.find({"email": email}))
        count = 0
        for record in users:
            count += 1
        if count < 1:
            return None
        else:
            return UserUtil.format_user(users[0])

    def update_token(self, email, token):
        query = { "email": email}
        value = { "token": token}
        res = self.collection.update_one(query, { "$set": value})
        return res
