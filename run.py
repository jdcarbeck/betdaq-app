from betdaqAPI.baseclient import BaseClient


import config

def main():
    runStrat()
    


def runStrat():
    GreyHoundRacingID = 100008

    client = BaseClient(config.username, config.password)
    resp = client.readonly.get_event_sub_tree_no_selections([GreyHoundRacingID])
    a = resp.get("EventClassifiers")
    b = a[0]
    z = b.get("EventClassifiers")
    print(type(z))
    x = z[0]
    print(type(x))
    events= x.get(("EventClassifiers"))
    for i in events:
        for u in i.get("EventClassifiers"):
            for r in u.get("Markets"):
                print("\n\n==================")
                y = client.readonly.get_prices([r.get("Id")])

                for q in y.get("MarketPrices"):
                    for j in q.get("Selections"):
                        print(j.get("Name"))
                
                

           

    #print(v.get("ParentId"))

    #for element in v :
        #print("\n\n ============================= \n \n")
        #print(element)

        


    #for element in resp:
        #print(element[0])
        #print("=")

if __name__ == "__main__":
    main()



