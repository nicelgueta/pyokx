# pyokx 
![Downloads](https://img.shields.io/pypi/dm/pyokx) 
![Tests](https://github.com/nicelgueta/pyokx/actions/workflows/pyokx.yml/badge.svg)
## Installation

```shell
pip install pyokx
```

## Introduction

pyokx is a completely unofficial python API wrapper developed to interact with the OKX V5 API. 
It's unique insofar as that it has been developed by scraping the API documentation to dynamically generate python code to provide an intuitive
pythonic interface for exact same API. This idea essentially is to avoid the need to create separate documentation for this wrapper and instead you can simply refer to the official OKX docs for API usage.

It's used by creating a base client instance to make and receive requests and passing that client to each API class (`APIComponent`), which has been dynamically generated from the API docs.


**Let's start with an example.**

Let's say we want to check all current positions.

Check out the docs for get balance here: https://www.okx.com/docs-v5/en/#rest-api-account-get-positions

We can see the endpoint belongs to the Account API and needs to be called with 3 parameters:
![OKX-docs](get-pos.png)

In pyokx, you can see the method signature for the Account class is exactly the same:
```python
def get_positions(
        self,
        instType: str = None,
        instId: str = None,
        posId: str = None,
        use_proxy: bool = False,
    ) -> APIReturn:
```

So this can be easily implemented like so:

1. Create `.env` file that contains your API information:
```
    KEY = replace_your_key_here
    SECRET = replace_your_secret_here
    PASSPHRASE = replace_your_passphrase_here
```

2. Read API information from `.env` and create the base client:
```python
import os

# python-dotenv should have been installed from the dependencies
from dotenv import load_dotenv
from pyokx import OKXClient, Account

# read information from .env file
load_dotenv()

# create the base client:
client = OKXClient(
    key = os.getenv('KEY'),
    secret = os.getenv('SECRET'),
    passphrase = os.getenv('PASSPHRASE'),
)
...
```

3. Now you can create Account object and call endpoints
```python
...
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
```

That simple.

______


## Key features

### APIReturn

This is essentially a wrapper around the response that is returned from every endpoint. This is to provide some useful helper methods such as dataframe conversion.

### Proxies

As is common with a lot of exchange APIs, for calls that require authentication (usually account/trade-related), it is strongly encouraged to limit your API key to a select list IP addresses to protect your account. On some systems this may require routing traffic through a forward proxy. pyokx supports this pattern by allowing you to pass the necessary proxies to the base client and you can trigger this behaviour by setting the `use_proxy` parameter to `True`.
For example:
```python
proxies = {
    "http": "http://your-proxy-server.com",
    "https": "https://your-proxy-server.com",
}
client = OKXClient(
    key="key",
    secret="secret",
    passphrase="passphrase",
    proxies=proxies
)

# trigger the use of the proxy server with use_proxy
account = Account(client)
api_response = account.get_positions(use_proxy=True)

```

## Development progress

**It's still a very early version - so issues, feature requests and bugs are very welcome!**

- [x] REST API implementation.
- [ ] Fix pythonic naming conventions when API names contain special characters
- [ ] Enhance documentation
- [ ] Websocket API implementation. 

## Disclaimer
> NB. pyokx is totally unofficial and is in no way affiliated with OKEX Crypto exchange and simply exists as a helpful wrapper to interact with the V5 API.