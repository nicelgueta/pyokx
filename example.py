import os
from dotenv import load_dotenv
from pyokx import OKXClient, Account

# read user information from .env file 
load_dotenv()

# create the base client:
client = OKXClient(
    key = os.getenv('KEY'),
    secret = os.getenv('SECRET'),
    passphrase = os.getenv('PASSPHRASE'),
)

# create a component for the Account API by passing the client dependency
account = Account(client)

# get positions
api_response = account.get_positions()

# you can convert to a pandas dataframe to make it more readable
df_response = api_response.to_df()
print(df_response)

# or you can get the raw response
raw_response = api_response.response
print(raw_response)
