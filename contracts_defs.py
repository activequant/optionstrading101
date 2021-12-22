from ib_insync import *


fdax = Contract()
fdax.symbol = "DAX"
fdax.secType = "FUT"
fdax.exchange = "DTB"
fdax.currency = "EUR"
fdax.lastTradeDateOrContractMonth = "202112"
fdax.multiplier = 25



class Dax:
    underlying = Index('DAX')
    price_source = fdax
    options_config = {
        'min_exp':0, # min days to expiry
        'num_strikes':3
    }
    
