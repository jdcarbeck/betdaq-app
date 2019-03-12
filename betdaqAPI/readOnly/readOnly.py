import zeep
from betdaqAPI.baseclient import BaseClient
#all the readonly go in here
#this clase baseclient and use the readonly part of it

#implement testing (BONUS!!)

class ReadOnly(BaseClient):

    def listTopLevelEvents(self, wantPlayMarkets):
        return self.client.service.ListTopLevelEvents(wantPlayMarkets)

    def GetEventSubTreeNoSelections(self, handle, wantDirectDescendantsOnly, wantPlayMarkets)
        return self.client.service.GetEventSubTreeNoSelections(handle, wantDirectDescendantsOnly, wantPlayMarkets)

    def GetEventSubTreeWithSelections(self, handle, wantPlayMarkets)
        return self.client.service.GetEventSubTreeNoSelections(handle, wantPlayMarkets)

    def GetMarketInformation(self, handle)
        return self.client.service.GetMarketInformation(handle)

    def ListSelectionsChangedSince(self, selectionSequenceNumber)
        return self.client.service.ListSelectionsChangedSince(selectionSequenceNumber)

        



    #create a client for the method below to use

    #create a function for every readonly in API doc 25-36 and check parameters
    #11 functions to be implemented TODO: THURSDAY
    #TODO: CIAN 8-11
    #TODO: BRIAN 5-8
    #TODO: JOESEPH 1-4
