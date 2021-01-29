from Logic import TokenHandler
from Logic import ForceBridgeConnector

user = "GitHub"
password = "GitHub"
urlToken = "https://forcebridgehackathon.force.eco:25443/ffauth/oauth2.0/accessToken?client_id=" + user + "&client_secret=" + password + "&grant_type=client_credentials&scope=read%20write"
urlToBridgeAPI = "https://forcebridgehackathon.force.eco:24443/ffwebservices/api/v3/"
workplaceNumber = "R_WPL_04"

print("Welcome to the get current operating state of a workplace example!\n")
print("Determine token ...\n")

tokenhandler = TokenHandler.TokenHandler
tokeninit = tokenhandler(user, password, urlToken)
token = tokeninit.GetAccessToken()
accessToken = token['access_token']

print("Token: " + accessToken + "\n")
print("Determine workplace " + workplaceNumber + "...\n")

Connector = ForceBridgeConnector.FORCEBridgeConnector
BridgeConnector = Connector(urlToBridgeAPI, accessToken)
header = BridgeConnector.Tokenheader(accessToken)
operatingStates = BridgeConnector.GetWorkplaceByNumber(header, workplaceNumber)

print("Workplace: {} ({})".format(operatingStates['_embedded']['workplaces'][0]['properties']['number'], operatingStates['_embedded']['workplaces'][0]['properties']['description']))
print("State: {}: {} (Id: {})".format(operatingStates['_embedded']['workplaces'][0]['properties']['operatingState']['code'],
                                      operatingStates['_embedded']['workplaces'][0]['properties']['operatingState']['description'],
                                      operatingStates['_embedded']['workplaces'][0]['properties']['operatingState']['id']))
