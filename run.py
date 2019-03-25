from betdaqAPI.baseclient import BaseClient
from betdaqAPI.enums import MarketStatus
from betdaqAPI.enums import MarketType

import config

def main():
    GreyHoundRacingID = 100008
    client = BaseClient(config.username, config.password)
    run2(client,GreyHoundRacingID)
    

def runStrat(client,id):
    
    _event_Classifier = "EventClassifiers"
    _markets = "Markets"
    _market_Type = "Type"
    _Id = "Id"


    #Get The Sport's Substree
    resp = client.readonly.get_event_sub_tree_no_selections(id)
    a = resp.get(_event_Classifier)
    b = a[0]
    z = b.get(_event_Classifier)
    print(type(z))
    x = z[0]
    print(type(x))
    allMeets = x.get(_event_Classifier)
    for meet in allMeets:
        for u in meet.get(_event_Classifier):
            for r in u.get(_markets):
                if r.get(_market_Type) is MarketType.Win.value:
                    y = client.readonly.get_prices([r.get(_Id)])
                    for q in y.get("MarketPrices"):
                        for j in q.get("Selections"):
                            print("\n\n",j)
                            print(j.get("Name"))
                            

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
    for meet in allMeets:
        meet_name = meet.get(_name)
        meet_id = meet.get(_Id)
        print("\n\n",meet_name)
        for race in meet.get(_event_Classifier):
            
            race_name = race.get(_name)

            for market in race.get(_markets):
                #print(market)
                print(race_name," time is ",market.get(_time), " for market type =  ", MarketType(market.get(_market_Type)))



        #     for r in u.get(_markets):
        #         if r.get(_market_Type) is MarketType.Win.value:
        #             y = client.readonly.get_prices([r.get(_Id)])
        #             for q in y.get("MarketPrices"):
        #                 for j in q.get("Selections"):
        #                     print("\n\n", j)
        #                     print(j.get("Name"))
def run2(client, id):

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
    for meet in allMeets:
        meet_name = meet.get(_name)
        meet_id = meet.get(_Id)
        print("\n\n", meet_name)
        for race in meet.get(_event_Classifier):

            race_name = race.get(_name)

            for market in race.get(_markets):
                #print(market)
                print(race_name, " time is ", market.get(
                    _time), " for market type =  ", MarketType(market.get(_market_Type)))

        #     for r in u.get(_markets):
        #         if r.get(_market_Type) is MarketType.Win.value:
        #             y = client.readonly.get_prices([r.get(_Id)])
        #             for q in y.get("MarketPrices"):
        #                 for j in q.get("Selections"):
        #                     print("\n\n", j)
        #                     print(j.get("Name"))
if __name__ == "__main__":
    main()



