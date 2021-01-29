import requests


class FORCEBridgeConnector:

    baseURL = "https://forcebridgehackathon.force.eco:24443/ffwebservices/api/v3/"
    accessToken = ""
    head = ""
    workplaceNumber = ""

    def __init__(self, baseURL, accessToken):
        self.baseURL = baseURL
        self.accessToken = accessToken

    def Tokenheader(self, accessToken):
        head = {'Accept-Language': 'en-EN', 'accept': 'application/json;charset=UTF-8',
                'Authorization': 'Bearer {}'.format(accessToken)}
        self.head = head
        return head

    def GetWorkplaces(self, head):
        self.baseURL = self.baseURL + "workplaces"
        workplaces = requests.get(self.baseURL, headers=head).json()
        return workplaces

    def GetWorkplaceByNumber(self, head, workplaceNumber):
        self.baseURL = self.baseURL + "workplaces?workplaceNumber=" + workplaceNumber
        workplaceByNumber = requests.get(self.baseURL, headers=head).json()
        return workplaceByNumber

    def GetOperatingStates(self, head):
        self.baseURL = self.baseURL + "masterData/operatingStates"
        operatingStates = requests.get(self.baseURL, headers=head).json()
        return operatingStates
