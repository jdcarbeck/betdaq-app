from betdaqAPI.baseclient import BaseClient
from betdaqAPI.enums import MarketStatus
from betdaqAPI.enums import MarketType

import config
import time

def main():
    GreyHoundRacingID = 100008
    client = BaseClient(config.username, config.password)
    # timeAndMarket(client, GreyHoundRacingID)
    runStart(client,GreyHoundRacingID)
    # runOrderWithMinBal(client,100)
    # print(getGBPAvailableFunds(client))
    # mids = getSportMarketsByType(client, GreyHoundRacingID, MarketType.Win)    

def runStart(client,SportId):
    #Getting Sport Markets
    print("##### == ", "Getting Sport Markets", " == #####")
    mids = getSportMarketsByType(client, SportId, MarketType.Win)
    print("##### == ", "Market Collection Complete", " == #####")
    print("##### == ", "Checking Market Time", " == #####")
    currentTime = getApiTime(client)
    print("##### == ", "Market Time is ",currentTime, " == #####")
    print("##### == ", "Getting Market Times", " == #####")
    timeDict = getMarketTimes(client, mids)
    print("##### == ", "Found Market Times", " == #####")
    print(timeDict)


    while(True):
        time.sleep(10)
        print(getApiTime(client))


def runOrderWithMinBal(client,minBal,order):
    return 0

def activeOrderForID(client, id):

    return True

def getGBPAvailableFunds(client):
    resp = client.secure.get_account_balances()
    return resp.get("AvailableFunds")


def split(seq, num):
    avg = len(seq) / float(num)
    out = []
    last = 0.0
    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return out

#Submit Client, Sport ID and recieve all market ID's in return
def getSportMarketsByType(client,sportID,marketType):
    
    #JSON Names
    _event_Classifier = "EventClassifiers"
    _markets = "Markets"
    _name = "Name"
    _market_Type = "Type"
    _Id = "Id"
    _time = "StartTime"

    #
    # Return Value
    market_ids = []
    #
    #

    #Get The Sport's Substree
    resp = client.readonly.get_event_sub_tree_no_selections(sportID)

    #Unwrapped response
    sport_unwrapped = resp.get(_event_Classifier)
    
    #gets the subtree
    daily_unwrapped = getNextLevel(sport_unwrapped,_event_Classifier)

    #Gets all the Meets/Event Days
    meets_unwrapped = getNextLevel(daily_unwrapped,_event_Classifier)

    for meet in meets_unwrapped:
        for race in meet.get(_event_Classifier):
            # race_name = race.get(_name)
            for market in race.get(_markets):
                mar_type = MarketType(market.get(_market_Type))
                if mar_type is marketType:
                    m_id = market.get(_Id)
                    market_ids.append(m_id)

    return market_ids


def getNextLevel(input, identifier):
    c = input[0]
    return c.get(identifier)

def getApiTime(client):
    time = client.readonly.get_sp_enabled_markets_information().get("Timestamp")
    return time


def timeAndMarket(client, id):
    _event_Classifier = "EventClassifiers"
    _markets = "Markets"
    _name = "Name"
    _market_Type = "Type"
    _Id = "Id"
    _time = "StartTime"
    #Get The Sport's Substree
    resp = client.readonly.get_event_sub_tree_no_selections(id)
    a = resp.get(_event_Classifier)
    b = a[0]
    z = b.get(_event_Classifier)
    print(type(z))
    x = z[0]
    print(type(x))
    allMeets = x.get(_event_Classifier)
    xrp = 1


    market_ids = []
    for meet in allMeets:
        meet_name = meet.get(_name)
        meet_id = meet.get(_Id)
        # print("Meet Name = ",meet_name)
        for race in meet.get(_event_Classifier):
            race_name = race.get(_name)
            for market in race.get(_markets):
                mar_type = MarketType(market.get(_market_Type))
                if mar_type is MarketType.Win:
                    # print(race_name," time is ",market.get(_time), " for market type =  ", MarketType(market.get(_market_Type)), " ID = ",market.get("Id"))
                    idz = market.get("Id")
                    market_ids.append(idz)


def getMarketTimes(client, mids):
    _market_Prices = "MarketPrices"
    markets = {}
    mids_list = split(mids,2)
    for mids in mids_list:
        mids_resp = client.readonly.get_prices(mids)
        a = mids_resp.get(_market_Prices)
        for e in a:
            id = e.get("Id")
            startTime = e.get("StartTime")
            markets[startTime] = id
    print(markets)
    dict(sorted(markets.items()))
    return markets



if __name__ == "__main__":
    main()



