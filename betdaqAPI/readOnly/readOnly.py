from betdaqAPI.baseclient import BaseClient

#all the readonly go in here
#this clase baseclient and use the readonly part of it

#implement testing (BONUS!!)

class ReadOnly:
    
    def __init__(self, username, password):
        base = BaseClient(username, password)

        def ListTopLevelEvents(self):
            base.ListTopLevelEvents
            


    #create a client for the method below to use

    #create a function for every readonly in API doc 25-36 and check parameters
    #11 functions to be implemented TODO: Tuesday
    