from suds.client import Client as SudsClient
from betdaqAPI.endpoints import readOnly, secure


class BaseClient:

    def __init__(self, username, password, language='en', application_identifier=None):
        """
        WSDL client header.
        :param username: Betdaq username
        :type str
        :param password: Betdaw password
        :type str
        """
        self.username = username
        self.password = password
        self.url_readonly = 'https://api.betdaq.com/v2.0/ReadOnlyService.asmx?WSDL'
        self.url_secure = 'https://api.betdaq.com/v2.0/Secure/SecureService.asmx?WSDL'
        self.version = '2.0'
        self.language = language
        self.application_identifier = application_identifier
        self._readonly_client = SudsClient(self.url_readonly)
        self._add_headers(False)
        self._secure_client = SudsClient(self.url_secure)
        self._add_headers(True)

        self.readonly = readOnly.Endpoint(self._readonly_client)
        self.secure = secure.Endpoint(self._secure_client)

 
    def _add_headers(self, is_secure=True):
        if is_secure:
            client = self._secure_client
        else:
            client = self._readonly_client
        token = client.factory.create('ExternalApiHeader')
        token._version = self.version
        token._username = self.username
        token._password = self.password
        token._languageCode = self.language
        token._applicationIdentifier = self.application_identifier
        client.set_options(soapheaders=token)

