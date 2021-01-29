import requests


class TokenHandler:
    user = ""
    password = ""
    urlToken = ""

    def __init__(self, user, password, urlToken):
        self.user = user
        self.password = password
        self.urlToken = urlToken

    def GetAccessToken(self):
        token = requests.get(self.urlToken).json()
        return token
