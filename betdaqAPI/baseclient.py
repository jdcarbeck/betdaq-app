import zeep

class BaseClient:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.wsdl_file = 'http://api.betdaq.com/v2.0/API.wsdl'
        self.settings = zeep.Settings(strict=False)
        self.readonly_client = self.initialise_wsdl()

    def initialise_wsdl(self):
        readonly_client = zeep.Client(wsdl=self.wsdl_file, settings=self.settings)
        readonly_client.set_default_soapheaders({'ExternalApiHeader':self.external_headers})
        return readonly_client

    @property
    def external_headers(self):
        return{ "version": 2.0,
                "languageCode": 'en',
                "username": self.username,
                "password": self.password,
                "applicationIdentifier": None}
