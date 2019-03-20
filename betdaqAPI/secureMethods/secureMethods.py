import zeep
from betdaqAPI.baseclient import BaseClient
import time

class secureMethods(BaseClient):

    #HearBeat Functions

    int threshholdMs = 0

    def RegisterHeartbeat(self,threshholdMs,heartbeatAction):
        self.threshholdMs = threshholdMs
        return self.client.service.RegisterHeartbeat(threshholdMs,heartbeatAction)

    def Pulse(self):
        return self.client.service.Pulse()

    def ChangeHeartbeatRegstration(self,threshholdMs):
        self.ChangeHeartbeatRegstration
        return self.client.service.ChangeHeartbeatRegstration(threshholdMs,heartbeatAction)

    def DeregisterHeartbeat(self):
        self.threshholdMs = 0
        return self.client.service.DeregisterHeartbeat()

    def Pulser(self):
        self.client.service.pulse()
        time.sleep(self.threshholdMs)


    #Rest of secureMethods

    def GetAccountBalances(self):
        self.client.service.GetAccountBalances()

    def ListAccountPostings(self,startTime, endTime):
        self.client.service.ListAccountPostings(startTime, endTime)

    def ListAccountPostingsById(self,transactionId):
        self.client.service.ListAccountPostingsById(transactionId)

    
