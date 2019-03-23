from betdaqAPI.endpoints.base import BaseEndpoint
from betdaqAPI.enums import PriceFormat

class Endpoint(BaseEndpoint):

    def list_top_level_events(self, want_play_markets=None):
        """
        Get list of sports and their IDs.
        :param want_play_markets: whether to return play or real markets, None is False
        :return: all sports available
        """
        return self.request('ListTopLevelEvents', 'ListTopLevelEventsRequest', _WantPlayMarkets=want_play_markets)

    