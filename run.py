import betdaqAPI.baseclient as API

def main():
    wdsl = API.initialise_wsdl("username","password")
    print wdsl

if __name__ == "__main__":
    main()
