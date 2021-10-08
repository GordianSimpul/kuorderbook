#!/bin/env python3

import json
import argparse
import requests


KuOrderBk='https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=%s-%s'
parser = argparse.ArgumentParser(description="KuCoin - Order Books for Trading Pair")

parser.add_argument('coins', metavar='coin', nargs='+')
args = parser.parse_args()

coin1 = args.coins[0]
coin2 = args.coins[1]

ku_response = requests.get(KuOrderBk % (coin1, coin2)) 
space=' '



if ku_response.status_code == 200 and 'application/json' in ku_response.headers.get('Content-Type',''):
    #print(ku_response.json)
    try:
        KuJSON = json.loads(str(ku_response.content.decode('utf-8')))
        KuBids = KuJSON['data']['bids']
        KuAsks = KuJSON['data']['asks']
        print("                          %4s - %4s                             " % (coin1, coin2))
        print("_____________BIDS_____________ | _____________ASKS_____________")
        k=0
        for bid in KuBids:
            print("%3.6f" % float(bid[0]),space*4,"- %8.4f" %  float(bid[1]),space*7, " %3.6f" % float(KuAsks[k][0]), space*4, "-  %7.4f"  %   float(KuAsks[k][1]))
            k += 1
    except:
        print("error reading JSON")
            
