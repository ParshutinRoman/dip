from pprint import pprint
import requests
import time
from urllib.parse import urlencode

# APP_ID = 5030613
#AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
USER_NAME = 'eshmargunov'
USER_ID = 171691064
TOKEN = '73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1'
VERSION = '5.101'

#https://api.vk.com/method/groups.get?user_id=171691064&access_token=73eaea320bdc0d3299faa475c196cfea1c4df9da4c6d291633f9fe8f83c08c4de2a3abf89fbc3ed8a44e1&v=5.101

class User():
    def __init__(self, USER_ID):
        self.userid = USER_ID
       # self.response = {}

    def group_list(self):
        #self.response = []
        self.groups = []
        params = {
            'v': VERSION,
            'user_id': USER_ID,
            'access_token': TOKEN,
            'extended': 1,
            'fields': 'members_count'
        }
        response = requests.get('https://api.vk.com/method/groups.get', params)
        response = response.json()['response']['items']
        for i in response:
            self.groups.append({'id': i['id'], 'name': i['name'], 'members_count': i['members_count']})

        return(self.groups)

    def friends_list(self):
        params = {
            'v': VERSION,
            'user_id': USER_ID,
            'access_token': TOKEN,
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        self.friends = response.json()['response']['items']

        return (self.friends)

    def gruppa_incognita(self):
        user1.group_list()
        user1.friends_list()
        self.asd = []
        # print(self.groups)
        # print(self.friends)

        for group in self.groups:

            group = group['id']
            for user in self.friends:
                time.sleep(0.3)
                params = {
                    'v': VERSION,
                    'user_id': user,
                    'access_token': TOKEN,
                    'group_id': group
                }
                response = requests.get('https://api.vk.com/method/groups.isMember', params)
                #response = response.json()
                self.asd.append({group: response.json()['response']})



        return (self.asd)






user1 = User(USER_ID)
print(user1.gruppa_incognita())


# friends.get
#
# groups.get
#
# groups.isMember
#
# users.search
#
# friends.search