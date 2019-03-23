from betdaqAPI.endpoints.base import BaseEndpoint
from betdaqAPI import enums


class Endpoint(BaseEndpoint):

    def get_account_balances(self):
        """
        Get summary of current balances.
        :return: account information for logged in user.
        :rtype: dict
        """
        return self.request('GetAccountBalances', 'GetAccountBalancesRequest')