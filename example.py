from pyokx import OKXClient, Account

# create the base client dependency
cli = OKXClient(
    key="key",
    secret="secret",
    passphrase="passphrase",
)

# create a component for the Account API by passing the client dependency
account = Account(cli)

# get positions
api_return = account.get_positions()

# to convert to a pandas dataframe
df = api_return.to_df()
print(df)

# to look at the raw response
response = api_return.response
print(response.status)
