
from app.utils.UserUtil import UserUtil, User
from app.utils.ExamUtil import ExamUtil
from app.models.Exam import Exam
from .__init__ import *


class UserRepo(BaseRepo):

    def __init__(self, collection: str="users") -> None:
        super().__init__()
        self.collection = self.mydb[collection]

    def create_user(self, user: User):
        res = self.collection.insert_one(user.__dict__)
        return res

    def delete_user(self, email: str):
        res = self.collection.delete_one({"email": email})
        return res

    def get_all_admin(self):
        admins = list(self.collection.find({"role": 1}))
        list_admins = []
        for record in admins:
            list_admins.append(UserUtil.format_info_user(record))
        return list_admins

    def get_info_user(self, email):
        users = list(self.collection.find({"email": email}))
        count = 0
        for record in users:
            count += 1
        if count < 1:
            return None
        else:
            return UserUtil.format_info_user(users[0])

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

    def get_users_in_room(self, room):
        users = list(self.collection.find({"room": room}))
        list_users = []
        for record in users:
            list_users.append(UserUtil.format_info_user(record))
        return list_users

    def update_admin(self, info: User):
        query = { "email": info.email}
        value = { "room": info.room,
                "fullname": info.fullname,
                "role": info.role,
                "position": info.position,
                "date_of_birth": info.date_of_birth,
                "url_avatar": info.url_avatar
                }
        res = self.collection.update_one(query, { "$set": value})
        return res

    def update_token(self, email, token):
        query = { "email": email}
        value = { "token": token}
        res = self.collection.update_one(query, { "$set": value})
        return res

    def update_password(self, email, hash_password):
        query = {"email": email}
        value = {"password": hash_password}
        res = self.collection.update_one(query, {"$set": value})
        return res

    def update_user(self, info: User):
        query = { "email": info.email}
        value = { "room": info.room,
                "fullname": info.fullname,
                "position": info.position,
                "date_of_birth": info.date_of_birth,
                "url_avatar": info.url_avatar
                }
        res = self.collection.update_one(query, { "$set": value})
        return res