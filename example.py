# load API keys from .env file
import dotenv

dotenv.load_dotenv()

import os

# creating a Base client
from pyokx.base import OKXClient

cli = OKXClient(
    key=os.getenv("OKX_API_KEY_TEST"),
    secret=os.getenv("OKX_API_SECRET_TEST"),
    passphrase=os.getenv("OKX_API_PHRASE_TEST"),
)
