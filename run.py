from betdaqAPI.readOnly.readOnly import ReadOnly
from betdaqAPI.utils import clean_locals
import config
import datetime

def main():
    # creates a base to use the clientgit
    read_client = ReadOnly(config.username, "")
    params = clean_locals(locals())
    response = read_client.request('ListTopLevelEvents', params)
    print(read_client.process_response(response, datetime.datetime.utcnow(), 'EventClassifiers'))
    # Ideally this is how we call functions

if __name__ == "__main__":
    main()
