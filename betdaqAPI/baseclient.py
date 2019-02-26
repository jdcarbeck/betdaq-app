import zeep

"""
    This is the base for the readonly_client and later the secure Client
    by creating this object using the service function from the zeep Client
    calls can be made to the api with the right parameters
"""
class BaseClient:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wsdl_file = 'http://api.betdaq.com/v2.0/API.wsdl'
        self.settings = zeep.Settings(strict=False)
        self.client = self.initialise_wsdl()

    def initialise_wsdl(self):
        # just initialises the readonly_client as of now can expand to secure
        client = zeep.Client(wsdl=self.wsdl_file, settings=self.settings)
        client.set_default_soapheaders({'ExternalApiHeader':self.external_headers})
        return client

    @property
    def external_headers(self):
        return{ "version": 2.0,
                "languageCode": 'en',
                "username": self.username,
                "password": self.password,
                "applicationIdentifier": None }
