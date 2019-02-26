from betdaqAPI.readOnly import ReadOnly
from betdaqAPI.baseclient import BaseClient
import config

def main():
    # creates a base to use the readonly_client and eventually secure client
    base = BaseClient("username", "password")
    #sample of creating a call, requesting top events from api

    # print(readonly.ListTopLevelEvents())

    # Ideally this is how we call functions
    # base.ListTopLevelEvents()

if __name__ == "__main__":
    main()
