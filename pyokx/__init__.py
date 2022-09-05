from loguru import logger
import sys
from .Account import Account
from .Blocktrading import Blocktrading
from .Convert import Convert
from .Earn import Earn
from .Funding import Funding
from .Gridtrading import Gridtrading
from .Marketdata import Marketdata
from .Publicdata import Publicdata
from .Status import Status
from .SubAccount import SubAccount
from .Trade import Trade
from .Tradingdata import Tradingdata
from .base import OKXClient


__version__ = "0.3.0"


def change_log_level(level: str = "INFO"):
    logger.remove()
    logger.add(sys.stdout, level=level)


change_log_level()

__all__ = [
    "Account",
    "Blocktrading",
    "Convert",
    "Earn",
    "Funding",
    "Gridtrading",
    "Marketdata",
    "Publicdata",
    "Status",
    "SubAccount",
    "Trade",
    "Tradingdata",
    "change_log_level",
    "OKXClient",
]
