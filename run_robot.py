import time as true_time
import pprint
import pathlib

from datetime import datetime
from datetime import timedelta
from configparser import ConfigParser

from pyrobot.robot import PyRobot
from pyrobot.indicator import Indicators

# Grab the config file
config = ConfigParser()
config.read('configs/config.ini')

CLIENT_ID = config.get('main', 'CLIENT_ID')
REDIRECT_URI = config.get('main', 'REDIRECT_URI')
CREDENTIALS_PATH = config.get('main', 'JSON_PATH')
ACCOUNT_NUMBER = config.get('main', 'ACCOUNT_NUMBER')

# Initialize the robot.
trading_robot = PyRobot(
    client_id=CLIENT_ID,
    redirect_uri=REDIRECT_URI,
    credentials_path=CREDENTIALS_PATH,
    trading_account=ACCOUNT_NUMBER,
    paper_trading=True
)

# Create a new portfolio.
trading_robot_portfolio = trading_robot.create_portfolio()

# Add multiple positions to our portfolio.
multi_position = [
    {
        'asset_type': 'equity',
        'quantity': 2,
        'purchase_price': 4.00,
        'symbol': 'TSLA',
        'purchase_date': '2024-01-19'
    },
    {
        'asset_type': 'equity',
        'quantity': 2,
        'purchase_price': 4.00,
        'symbol': 'SQ',
        'purchase_date': '2024-01-19'
    },
]

# Add those positions to the portfolio.
new_positions = trading_robot.portfolio.add_positions(positions=multi_position)
pprint.pprint(new_positions)