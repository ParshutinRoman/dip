from pprint import pprint
import requests
from urllib.parse import urlencode

# APP_ID = 5030613
#AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
USER_NAME = 'eshmargunov'
USER_ID = 171691064
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
VERSION = '5.101'

class User():
    def __init__(self, USER_ID):
        self.userid = USER_ID
        self.response = {}


    def group_list(self):
        self.response = []
        params = {
            'v': VERSION,
            'user_id': USER_ID
        }
        response = requests.get('https://api.vk.com/method/groups.get', params)
        response = response.json()['response']
        self.response = response.get('items')
        return(response)

    def __str__(self):
        for id in self.response:
            print("id общего друга " + str(id))

    # def __str__(self):
    #     print(self.response)
    # #print(response)

user1 = User(USER_ID)
print(user1)

# friends.get
#
# groups.get
#
# users.search
#
# friends.search