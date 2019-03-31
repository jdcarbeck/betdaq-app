from betdaqAPI.baseclient import BaseClient
from betdaqAPI.enums import MarketStatus
from betdaqAPI.enums import MarketType
from betdaqAPI.enums import Polarity
from betdaqAPI.enums import WithdrawRepriceOption
from betdaqAPI.enums import OrderKillType
from datetime import datetime
from datetime import timedelta


import betUtils
import config
import time

RunStrat1 = True

def main():
    GreyHoundRacingID = 100008
    client = BaseClient(config.username, config.password)
    # timeAndMarket(client, GreyHoundRacingID)
    #runBidExecution(client, [15085063])
    runStart(client,GreyHoundRacingID)
    
    
    
    # activeOrderForID(client, [15047743])
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
    print("##### == ", "Program Now Running", " == #####")
    print("##### == ", "Loop Running Every 10 Seconds", " == #####")
    
    while(RunStrat1):
        time.sleep(10)
        currTime = getApiTime(client)
        delList = []
        for r in timeDict:
            if (r-currTime).seconds < 120 :
                runBidExecution(client, timeDict[r])
                delList.append(r)
        for tmp in delList:
            del timeDict[tmp]
        print("##### == ", "No Markets Found at ",currTime , " == #####")


def runBidExecution(client,bidID):
    ret = execute(client, bidID,2,5,0.01)
    return ret

def getNo1DisplayOrderCode(client,bidId):
    a = client.readonly.get_market_information(bidId)
    bets = a.get("Markets")[0]
    selections = bets.get("Selections")
    for select in selections:
        if select.get("DisplayOrder") is 1:
            return select.get("Id")
    return 0

def execute(client,betId,lower,upper,stakeVal):
    a = client.readonly.get_prices(betId)
    bets = a.get("MarketPrices")
    things = bets[0].get("Selections")
    x = 1
    for select in things:
        if x is 1:
            pricesDict = select.get("ForSidePrices")
            price = (pricesDict[0].get("Price"))
            if price < lower:
                print("##### == ", select.get("Name"),
                      " price was too low for bounds at = ", price, " == #####")
                return False
            if price > upper:
                print("##### == ", select.get("Name")," price was too high for bounds at = ", price, " == #####")
                return False
            
            print("##### == ", select.get("Name"), " is within bounds at = ", price, " == #####")
            print("##### == ","Making Order", " == #####")

            # Do Order
            order = place_order(
                selection_id= select.get("Id"),
                stake=stakeVal,
                price=price+.3,
                polarity=Polarity.back.value,
                expected_selection_reset_count=0,
                expected_withdrawal_sequence_number=0,
                expires_at=datetime.utcnow() + timedelta(days=1)
            )
            print("##### == ","Funds = ",getGBPAvailableFunds(client), " == #####")
            print("##### == ", "Starting 5 Second Delay to cancel", " == #####")
            time.sleep(5)
            print("##### == ", "Sending Order", " == #####")
            reciept = client.secure.place_orders_with_receipt(orders=[order])
            print("##### == ", "Order Sent", " == #####")
            print("##### == ", reciept, " == #####")
            print("##### == ", "Funds = ", getGBPAvailableFunds(client), " == #####")

            x =0
            return True




        
    return True



def activeOrderForID(client, id):
    print(client.secure.register_heartbeat())
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
    return markets


def place_order(
        selection_id,
        stake,
        price,
        polarity,
        expected_selection_reset_count,
        expected_withdrawal_sequence_number,
        cancel_on_in_running=True,
        cancel_if_selection_reset=True,
        expires_at=None,
        withdrawal_reprice_option=WithdrawRepriceOption.Cancel.value,
        kill_type= OrderKillType.FillOrKillDontCancel.value,
        fill_or_kill_threshold=0.0,
        punter_reference_number=1
):

    resp = {
        '_SelectionId': selection_id,
        '_Stake': stake,
        '_Price': price,
        '_Polarity': polarity,
        '_ExpectedSelectionResetCount': expected_selection_reset_count,
        '_ExpectedWithdrawalSequenceNumber': expected_withdrawal_sequence_number,
        '_CancelOnInRunning': cancel_on_in_running,
        '_CancelIfSelectionReset': cancel_if_selection_reset,
        '_WithdrawalRepriceOption': withdrawal_reprice_option,
        '_KillType': kill_type,
        '_FillOrKillThreshold': fill_or_kill_threshold,
        '_PunterReferenceNumber': punter_reference_number
    }
    if expires_at is not None:
        resp['_ExpiresAt'] = expires_at

    return resp

if __name__ == "__main__":
    main()
