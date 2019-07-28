
# basically all constants will be defined in this settings.py file

MKT_DATA_BASICS = ['open', 'low', 'close', 'high', 'volume']
BACKTEST_CURRENCIES = ['ETH-USD', 'BTC-USD', 'LTC-USD', 'ZEC-USD']

PERIODS = ['weekly', 'daily', 'minute']
BATCH_TEST_MODE = False
MINUTE_PERIODS_PER_YEAR = 525600
DAILY_PERIODS_PER_YEAR = 365
WEEKLY_PERIODS_PER_YEAR = 52
RISK_FREE_RATE = .0187  # U.S. Two Year Yield

CURRENT_PERIOD_SETTING = PERIODS[1]
CPY = DAILY_PERIODS_PER_YEAR
LONG_SMA_PERIOD = 15
SHORT_SMA_PERIOD = 7

DEBUG = False
