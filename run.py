from betdaqAPI.readOnly.readOnly import ReadOnly

import config

def main():
    read_client = ReadOnly(config.username, "")
    print(read_client.get_live_sports())
    
if __name__ == "__main__":
    main()
