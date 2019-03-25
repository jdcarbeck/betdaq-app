from betdaqAPI.baseclient import BaseClient

import config

def main():
    client = BaseClient(config.username, config.password)
    resp = client.readonly.list_top_level_events(False)
    print(resp)
    resp = client.secure.get_account_balances()
    print(resp)
    
if __name__ == "__main__":
    main()
