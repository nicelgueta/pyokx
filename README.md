# pyokx

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

```python
from pyokx.base import OKXClient
from pyokx.Account import Account

# create the base client dependency
cli = OKXClient(
    key="key",
    secret="secret",
    passphrase="passphrase",
)

# create a component for the Account API by passing the client dependency
a = Account(cli)

# get positions
api_return = a.get_positions()

# to convert to a pandas dataframe
df = api_return.to_df()

# to look at the raw response
response = api_return.response

```

That simple.

## Key features

### APIReturn

This is essentially a wrapper around the response that is returned from every endpoint. This is to provide some useful helper methods such as dataframe conversion.

## Development progress

**It's still a very early version - so issues, feature requests and bugs are very welcome!**

- [x] REST API implementation.
- [ ] Fix pythonic naming conventions when API names contain special characters
- [ ] Enhance documentation
- [ ] Websocket API implementation. 

## Disclaimer
> NB. pyokx is totally unofficial and is in no way affiliated with OKEX Crypto exchange and simply exists as a helpful wrapper to interact with the V5 API.