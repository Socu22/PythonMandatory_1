# PythonMandatory_1

## in vs code you can clone it when pressing file in the top left. --> New Window. --> Clone Git Repository.

## Setup 
  #setup .venv
    python -m venv .venv
    python3 -m venv .venv
  #activate .venv
    .venv\Scripts\activate        # Windows
    source .venv/bin/activate    # Linux/macOS 
  #Check if you use the currect python though 
    which python (MAC/LINUX/gitbash(windows))
    where python (Windows)

  # install dependencies 
    pip install -r requirements.txt
        ## if dependencies makes a ModuleNotFoundError: No module named 'requests'
            python -m pip install requests
            python -m pip install dotenv


## To use 
    ## make .env folder/package 
        with a API_Key = 'XXXXXXX'. in it. Get yours for free from https://www.exchangerate-api.com/
        
        Command:     python valuta.py --from DKK --to USD --amount 637.68
    ## or use the optional argument --key when using the Command-Line Interface.
            python valuta.py --key API_KEY_INSERTED --from DKK --to USD --amount 637.68

## Extra help 
    ## check the api 
        https://v6.exchangerate-api.com/v6/API_KEY_INSERTED/latest/
    ## help in the command
        you can use the optional argument -h to get insights into the command when using it. mainly to see exceptions or syntax errors. 