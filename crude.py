# simple option pnl tracker ... 
from ib_insync import *
import math
import pandas as pd
import math
from datetime import datetime, date, timedelta
import time
from collections import deque
from contracts_defs import *

util.startLoop()

ib = IB()

ib.connect('127.0.0.1', 4001, clientId=1238)

underlying = Crude().underlying
contracts = ib.qualifyContracts(underlying)
print(f'Identified {contracts}')
underlying = contracts[0] # using first contract

ib.reqMarketDataType(4)

price_sources = ib.qualifyContracts(Crude().price_source)
print(f'Fetched {price_sources} price sources.')
price_source = price_sources[0]


[ticker] = ib.reqTickers(price_source)

ref_price = ticker.marketPrice()
ul_value = ref_price   # just for convenience

print(f'Ref price {ref_price} ... ')




# request option chains ...
chains = ib.reqSecDefOptParams(underlying.symbol, underlying.exchange, underlying.secType, underlying.conId)
# formatting for data frame .. 
df_chains = util.df(chains)
print(df_chains)


def get_next_chain(chains, ref_date, min_days_to_expiry):
    #
    minimal_date = ref_date + timedelta(days=min_days_to_expiry)
    print(f'Minimal expiry date: {minimal_date}')
    chain_candidate = None
    found_min_date = None
    for chain in chains:
        #print(chain)
        for expiry in chain.expirations:
            #print(expiry)
            exp_date = datetime.strptime(expiry, "%Y%m%d")
            if exp_date > minimal_date:
                if found_min_date == None:
                    found_min_date = exp_date
                    chain_candidate = chain
                # need to check if this is sooner than before 
                if exp_date < found_min_date:
                    found_min_date = exp_date
                    chain_candidate = chain
    return(chain_candidate)
                

base = datetime.today()
opt_chain = get_next_chain(chains, base, 2)
print(f'Relevant chain {opt_chain}')




ib.disconnect()
