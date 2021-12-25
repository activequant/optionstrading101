from ib_insync import *


fdax = Contract()
fdax.symbol = "DAX"
fdax.secType = "FUT"
fdax.exchange = "DTB"
fdax.currency = "EUR"
fdax.lastTradeDateOrContractMonth = "202112"
fdax.multiplier = 25

crude = Contract()
crude.symbol = "CL"
crude.secType = "FUT"
crude.exchange = "NYMEX"
crude.currency = "USD"
crude.lastTradeDateOrContractMonth = "202202"
crude.multiplier = 1000


class Dax:
    underlying = Index('DAX')
    price_source = fdax
    options_config = {
        'min_exp':0, # min days to expiry
        'num_strikes':3
    }
    
    
class Crude:
    underlying = crude
    price_source = crude
    options_config = {
        'min_exp':2, # min days to expiry
        'num_strikes':3,
        'option_type':'FOP'
    }
    
