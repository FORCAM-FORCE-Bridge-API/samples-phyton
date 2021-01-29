from Logic import TokenHandler
from Logic import ForceBridgeConnector

user = "GitHub"
password = "GitHub"
urlToken = "https://forcebridgehackathon.force.eco:25443/ffauth/oauth2.0/accessToken?client_id=" + user + "&client_secret=" + password + "&grant_type=client_credentials&scope=read%20write"
urlToBridgeAPI = "https://forcebridgehackathon.force.eco:24443/ffwebservices/api/v3/"


print("Welcome to the get all available workplaces sample!\n")
print("Determine token ...\n")

tokenhandler = TokenHandler.TokenHandler
tokeninit = tokenhandler(user, password, urlToken)
token = tokeninit.GetAccessToken()
accessToken = token['access_token']

print("Token: " + accessToken + "\n")
print("Determine workplaces ...\n")

Connector = ForceBridgeConnector.FORCEBridgeConnector
BridgeConnector = Connector(urlToBridgeAPI, accessToken)
header = BridgeConnector.Tokenheader(accessToken)
workplaces = BridgeConnector.GetWorkplaces(header)

for workplace in workplaces['_embedded']['workplaces']:
    workplaceId = workplace['properties']['id']
    workplaceNumber = workplace['properties']['number']
    workplaceDescription = workplace['properties']['description']
    print('Id: {}, Number: {}, Description: {}'.format(workplaceId, workplaceNumber, workplaceDescription))


