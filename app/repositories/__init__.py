import pymongo
from app.configs.Config import DBConfig
from app.constants.common import DB
class BaseRepo:
    def __init__(self):
        self.myclient = pymongo.MongoClient(DB.URL)
        self.mydb = self.myclient[DB.NAME]
        # print("aaaaaaaaaaaaa", self.myclient.server_info())

    # First step: create new db (db can co du lieu moi tao dc)
        # self.collection = self.mydb["users"]
        # mydict = {"email": "admin@gmail.com", "password": "admin", "role": "ADMIN", "subject": None, "fullname": "Test User", "dob": "01-01-1999", "avatar": "", "token": "", "username": "admin","list_subjects_id": [],}
        # x = self.collection.insert_one(mydict)
