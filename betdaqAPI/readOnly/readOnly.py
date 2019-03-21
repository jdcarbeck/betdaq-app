import datetime

import zeep
from betdaqAPI.baseclient import BaseClient

#all the readonly go in here
#this clase baseclient and use the readonly part of it

#implement testing (BONUS!!)

class ReadOnly(BaseClient):

    def request(self, method, params):
        response = self.client.service[method](params)
        data = zeep.helpers.serialize_object(response)
        return data

    def process_response(self, response, time_sent, target):
        return {
            'data' : response.get(target, []) if target else response,
            'time_sent' : time_sent,
            'time_rec' : datetime.datetime.utcnow(),
        }
