from betdaqAPI.baseclient import BaseClient
import config

def main():
    # creates a base to use the readonly_client and eventually secure client
    base = BaseClient(config.username, config.password)
    #sample of creating a call, requesting top events from api
    print(base.readonly_client.service.ListTopLevelEvents())

if __name__ == "__main__":
    main()
