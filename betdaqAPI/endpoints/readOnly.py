from betdaqAPI.endpoints.base import BaseEndpoint
from betdaqAPI.enums import PriceFormat

class Endpoint(BaseEndpoint):


        def list_top_level_events(self, want_play_markets=False):
        
            return self.request("ListTopLevelEvents", "ListTopLevelEventsRequest", _WantPlayMarkets=want_play_markets)
        
        def get_event_sub_tree_with_selections(self, event_handle, want_play_markets=False):

            return self.request("GetEventSubTreeWithSelections", "GetEventSubTreeWithSelectionsRequest", EventClassifierIds=event_handle,_WantPlayMarkets=want_play_markets)

        def get_event_sub_tree_no_selections(self, event_handle, want_direct_descendents_only=False,  want_play_markets=False):
            return self.request("GetEventSubTreeNoSelections","GetEventSubTreeNoSelectionsRequest",EventClassifierIds=event_handle,_WantDirectDescendentsOnly=want_direct_descendents_only,_WantPlayMarkets=want_play_markets)

    
