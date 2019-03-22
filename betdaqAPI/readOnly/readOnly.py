import datetime

import zeep
from betdaqAPI.baseclient import BaseClient
import betdaqAPI.utils as utils
from betdaqAPI.readOnly import parsers


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

    def get_live_sports(self):
        params = utils.clean_locals(locals())
        response = self.request('ListTopLevelEvents', params)
        data = self.process_response(response, datetime.datetime.utcnow(), 'EventClassifiers')
        return [parsers.parse_sports(sport) for sport in utils.list_check(data.get('data', []))] if data.get('data') else []

    def get_markets(self, market_ids):
        date_time_sent = datetime.datetime.utcnow()
        params = self.client.readonly_types['GetMarketInformationRequest'](
            _value_1=[{'MarketIds': m_id} for m_id in utils.list_check(market_ids)]
        )
        response = self.request('GetMarketInformation', params)
        data = self.process_response(response, date_time_sent, 'Markets')
        return data