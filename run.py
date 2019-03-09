from betdaqAPI.readOnly.readOnly import ReadOnly
from betdaqAPI.baseclient import BaseClient
import config

def main():
    # creates a base to use the client
    base = BaseClient("username", "password")

    read_client = ReadOnly(BaseClient(config.username, config.password))

    output = read_client.listTopLevelEvents()
    print(output)
    # Ideally this is how we call functions

if __name__ == "__main__":
    main()
