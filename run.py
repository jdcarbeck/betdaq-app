from betdaqAPI.baseclient import BaseClient
import config

def main():
    wdsl = BaseClient(config.username, config.password)
    print(wdsl.readonly_client.service.ListTopLevelEvents())

if __name__ == "__main__":
    main()
