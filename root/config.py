"""
© Mrvishal2k2
RenameBot
This file is a part of mrvishal2k2 rename repo
Dont kang !!!
© Mrvishal2k2
"""
import os


class Config(object):
    APP_ID = int(os.environ.get(25341724))
    API_HASH = os.environ.get("752a1fb86785c5bd35eb7b1e42071786")
    TG_BOT_TOKEN = os.environ.get("6129167866:AAGIEh5O1Zgt_9GLRc3pmaUq6VYeVvTca5o")
    AUTH_USERS = [int(x) for x in os.environ.get("AUTH_USERS", "5925926828 5860097723").split()]
    DOWNLOAD_LOCATION = os.environ.get("DOWNLOAD_LOCATION", "./bot/DOWNLOADS")
    DB_URI = os.environ.get("DATABASE_URL")
    # owner is for log cmd only owner can use (this can be multiple users)
    OWNER_ID = [int(i) for i in os.environ.get("5860097723 5925926828").split(" ")]
    OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "MonsterKatakuri")
    CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", False)
