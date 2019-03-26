from betdaqAPI.utils import to_dict, check_status_code
from betdaqAPI.exceptions import APIError

class BaseEndpoint:
    def __init__(self, parent):
        self.client = parent

    def request(self, method, param_name, **kwargs):
        try:
            method = getattr(self.client.service, method)
            params = self.create_params(param_name, **kwargs)
            resp = method(params)
        except Exception as e:
            raise APIError(None, method, params=kwargs, exception=e)
        return self.process_resp(resp)

    def create_params(self, param_name, **kwargs):
        r = self.client.factory.create(param_name)
        for k, i in kwargs.items():
            setattr(r, k, i)
        return r

    def process_resp(self, resp):
        response = to_dict(resp, self.client)
        check_status_code(response)
        return response