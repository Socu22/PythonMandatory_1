import argparse
import requests
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv() 

def get_api_key(provided_key):
    if provided_key:
        print("from optional argument --key: "+provided_key)
        return provided_key
    
    env_key = os.environ.get("API_KEY")
    if env_key:
        print("from .env API_KEY: "+env_key)
        return env_key
    
    print("No API key provided. Use --key or add API_KEY to .env file.")
    exit()



def convert_currency(api_key, from_currency, to_currency, amount):
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency}"
    
    response = requests.get(url)
    data = response.json()

    if data["result"] != "success":
        print("Error fetching exchange rate.")
        exit()
    else:
        print("Succes fetching exchange rate.")


    rate = data["conversion_rates"].get(to_currency) ## json data --> list data --> a conversion_rate value of the to_currency 
 
    if not rate:
        print("Invalid target currency.")
        exit()

    converted = amount * rate ## math 
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")


def main():
    parser = argparse.ArgumentParser(description="Currency Converter CLI")  ## auto handling of all arguments 

    parser.add_argument("--key", help="Your ExchangeRate API key") ## add of an optional argument / option 
    parser.add_argument("--from", dest="from_currency", required=True, help="Base currency (e.g., USD)") ## Positional argument / argument
    parser.add_argument("--to", dest="to_currency", required=True, help="Target currency (e.g., DKK)")## Positional argument / argument
    parser.add_argument("--amount", type=float, required=True, help="Amount to convert")## Positional argument / argument

    args = parser.parse_args() ## parses the arguments for the Command-Line Interface 

    api_key = get_api_key(args.key) ## function for getting the API_Key through either --key or in the .env as API_KEY

    convert_currency( ## inserts value of the arguments of the Command 
        api_key,
        args.from_currency.upper(),
        args.to_currency.upper(),
        args.amount
    )


if __name__ == "__main__":
    main()