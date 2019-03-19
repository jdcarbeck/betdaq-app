import zeep
from betdaqAPI.baseclient import BaseClient
#all the readonly go in here
#this clase baseclient and use the readonly part of it

#implement testing (BONUS!!)

class ReadOnly(BaseClient):

    def listTopLevelEvents(self):
        return self.client.service.ListTopLevelEvents()


#TODO: BRIAN 5-8
    def listSelectionsChangedSince(self,selectionSequenceNumber):
        return self.client.service.ListSelectionsChangedSince(selectionSequenceNumber)

    def listMarketWithdrawalHistory(self, handle):
        return self.client.service.ListMarketWithdrawalHistory(handle)

    def getPrices(self, currency, thresholdAmount, numberForPricesRequired, numberAgainstPricesRequired,handle,wantMarketMatchedAmount,wantSelectionsMatchedAmounts,wantSelectionMatchedDetails):
        return self.client.service.GetPrices(currency, thresholdAmount, numberForPricesRequired, numberAgainstPricesRequired,handle,wantMarketMatchedAmount,wantSelectionsMatchedAmounts,wantSelectionMatchedDetails)

   # def getPrices(self, currency, thresholdAmount, numberForPricesRequired, numberAgainstPricesRequired,handle):
    #    return self.client.service.GetPrices(currency, thresholdAmount, numberForPricesRequired, numberAgainstPricesRequired,handle)

    def getOddsLadder(self, priceFormat):
        return self.client.service.GetOddsLadder(priceFormat)

      #create a client for the method below to use

    #create a function for every readonly in API doc 25-36 and check parameters
    #11 functions to be implemented TODO: THURSDAY
    #TODO: CIAN 8-11
    #TODO: JOESEPH 1-4
    