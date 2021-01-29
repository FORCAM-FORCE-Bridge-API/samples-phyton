from Logic import TokenHandler

user = "GitHub"
password = "GitHub"
urlToken = "https://forcebridgehackathon.force.eco:25443/ffauth/oauth2.0/accessToken?client_id=" + user + "&client_secret=" + password + "&grant_type=client_credentials&scope=read%20write"

print("Welcome to the authentication sample!\n")
print("Determine token ...\n")

tokenhandler = TokenHandler.TokenHandler
tokeninit = tokenhandler(user, password, urlToken)
token = tokeninit.GetAccessToken()

print("Result ClientCredentials:")
print("-----------------")
print("Token: " + token['access_token'])
print("Refresh-Token: " + token['refresh_token'])
print("Token type: " + token['token_type'])
print("Expires in: " + str(token['expires_in']))
print("Scope: " + token['scope'])
