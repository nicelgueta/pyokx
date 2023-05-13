from loguru import logger
import sys
from .account import Account
from .block_trading import Blocktrading
from .convert import Convert
from .earn import Earn
from .funding import Funding
from .grid_trading import GridTrading
from .market_data import MarketData
from .public_data import PublicData
from .status import Status
from .subaccount import Subaccount
from .trade import Trade
from .trading_data import TradingData
from .base import OKXClient


__version__ = "0.7.0"


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
    "GridTrading",
    "MarketData",
    "PublicData",
    "Status",
    "Subaccount",
    "Trade",
    "TradingData",
    "change_log_level",
    "OKXClient",
]
