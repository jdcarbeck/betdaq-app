from betdaqAPI.endpoints.base import BaseEndpoint
from betdaqAPI.enums import PriceFormat


class Endpoint(BaseEndpoint):

    def list_top_level_events(self, want_play_markets=False):

        return self.request("ListTopLevelEvents", "ListTopLevelEventsRequest", _WantPlayMarkets=want_play_markets)

    def get_event_sub_tree_with_selections(self, event_handle, want_play_markets=False):

        return self.request("GetEventSubTreeWithSelections", "GetEventSubTreeWithSelectionsRequest", EventClassifierIds=event_handle, _WantPlayMarkets=want_play_markets)

    def get_event_sub_tree_no_selections(self, event_handle, want_direct_descendents_only=False,  want_play_markets=False):
        return self.request("GetEventSubTreeNoSelections", "GetEventSubTreeNoSelectionsRequest", EventClassifierIds=event_handle, _WantDirectDescendentsOnly=want_direct_descendents_only, _WantPlayMarkets=want_play_markets)

    def get_market_information(self, market_ids=None):
        return self.request('GetMarketInformation', 'GetMarketInformationRequest', MarketIds=market_ids)

    def list_market_withdrawal_history(self, market_id=None):
        return self.request("ListMarketWithdrawalHistory", "ListMarketWithdrawalHistoryRequest", _MarketId=market_id)

    def get_prices(self, market_ids=None, threshold_amount=0, number_for_prices_required=3, number_against_prices_required=3, want_market_matched_amount=False, want_selections_matched_amounts=False, want_selection_matched_details=False):
        return self.request("GetPrices", "GetPricesRequest", MarketIds=market_ids, _ThresholdAmount=threshold_amount, _NumberForPricesRequired=number_for_prices_required, _NumberAgainstPricesRequired=number_against_prices_required, _WantMarketMatchedAmount=want_market_matched_amount, _WantSelectionsMatchedAmounts=want_selections_matched_amounts, _WantSelectionMatchedDetails=want_selection_matched_details,)

    def get_odds_ladder(self, price_format=PriceFormat.Decimal.value):
        return self.request("GetOddsLadder", "GetOddsLadderRequest", _PriceFormat=price_format)

    def get_list_selections_changed_since(self, selection_sequence_number=0):

        return self.request('ListSelectionsChangedSince', 'ListSelectionsChangedSinceRequest', _SelectionSequenceNumber=selection_sequence_number)

    def get_current_selection_sequence_number(self):
        return self.request(
            'GetCurrentSelectionSequenceNumber', 'GetCurrentSelectionSequenceNumberRequest')

    def list_selection_trades(self, selection_info, currency="GBP"):
        return self.request('ListSelectionTrades', 'ListSelectionTradesRequest', selectionRequests=selection_info, _currency=currency
                            )

    def get_sp_enabled_markets_information(self):
        return self.request('GetSPEnabledMarketsInformation', 'GetSPEnabledMarketsInformationRequest')
