from betdaqAPI.baseclient import BaseClient

import config

def main():
    client = BaseClient(config.username, config.password)
    resp = client.readonly.list_top_level_events()
    print(resp)
    # resp = read_client.get_all_events()
    # print(resp)
    # read_client.get_live_sports()
    
if __name__ == "__main__":
    main()
