from betdaqAPI.readOnly.readOnly import ReadOnly
import config

def main():
    # creates a base to use the client
    read_client = ReadOnly(config.username, "")

    print(read_client.listMarketWithdrawalHistory(1000))
    # Ideally this is how we call functions

if __name__ == "__main__":
    main()
