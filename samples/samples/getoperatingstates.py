from Logic import TokenHandler
from Logic import ForceBridgeConnector

user = "GitHub"
password = "GitHub"
urlToken = "https://forcebridgehackathon.force.eco:25443/ffauth/oauth2.0/accessToken?client_id=" + user + "&client_secret=" + password + "&grant_type=client_credentials&scope=read%20write"
urlToBridgeAPI = "https://forcebridgehackathon.force.eco:24443/ffwebservices/api/v3/"

print("Welcome to the get all operating states example!\n")
print("Determine token ...\n")

tokenhandler = TokenHandler.TokenHandler
tokeninit = tokenhandler(user, password, urlToken)
token = tokeninit.GetAccessToken()
accessToken = token['access_token']

print("Token: " + accessToken + "\n")
print("Determine operating states ...\n")

Connector = ForceBridgeConnector.FORCEBridgeConnector
BridgeConnector = Connector(urlToBridgeAPI, accessToken)
header = BridgeConnector.Tokenheader(accessToken)
operatingStates = BridgeConnector.GetOperatingStates(header)

for operatingstate in operatingStates['_embedded']['operatingStates']:
    stateCode = operatingstate['properties']['code']
    shortDescription = operatingstate['properties']['shortDescription']
    description = operatingstate['properties']['description']
    color = operatingstate['properties']['color']
    print("Operating state: {}: {} ({}) with color {}".format(stateCode, shortDescription, description, color))
