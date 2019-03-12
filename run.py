from betdaqAPI.readOnly.readOnly import ReadOnly
import config

def main():
    # creates a base to use the clientgit
    read_client = ReadOnly(config.username, "")

    print(read_client.listTopLevelEvents(True))
    # Ideally this is how we call functions

if __name__ == "__main__":
    main()
