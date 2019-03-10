import zeep
from betdaqAPI.baseclient import BaseClient
#all the readonly go in here
#this clase baseclient and use the readonly part of it

#implement testing (BONUS!!)

class ReadOnly(BaseClient):

    def listTopLevelEvents(self):
        return self.client.service.ListTopLevelEvents()


#TODO: BRIAN 5-8
    def listSelectionsChangedSince(self):
        return self.client.service.ListSelectionsChangedSince()

    def listMarketWithdrawalHistory(self, long Market):
        return self.client.service.ListMarketWithdrawalHistory()

    def getPrices(self, String currency, MoneyAmount thresholdAmount, int numberForPricesRequired,int numberAgainstPricesRequired):
        return self.client.service.GetPrices()

    def getOddsLadder(self, PriceFormat priceFormat):
        return self.client.service.GetOddsLadder()

      #create a client for the method below to use

    #create a function for every readonly in API doc 25-36 and check parameters
    #11 functions to be implemented TODO: THURSDAY
    #TODO: CIAN 8-11
    #TODO: JOESEPH 1-4
    