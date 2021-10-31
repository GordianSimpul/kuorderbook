#!/bin/env python3

import json
import argparse
import requests
from subprocess import call


space=' '

def kucoin_logo():
    with open('kucoin.uni') as logoFile:
        logo = logoFile.readlines()
    for line in logo:
        print(10*space,line, end='')
        
def get_kucoin_order_books(coin1, coin2, args):
    KuOrderBk='https://api.kucoin.com/api/v1/market/orderbook/level2_20?symbol=%s-%s'
    
    try:
        trade_amt = float(args.amount)
        target_amt = float(args.target)
    except TypeError as e:
        if trade_amt:
            pass
        if not trade_amt and not target_amt:
            trade_amt = target_amt = None
        else:
            target_amt=None
    
    ku_response = requests.get(KuOrderBk % (coin1, coin2)) 
    
    
    if ku_response.status_code == 200:
        try:
            KuJSON = json.loads(str(ku_response.content.decode('utf-8')))
            KuBids = KuJSON['data']['bids']
            KuAsks = KuJSON['data']['asks']
            kucoin_logo()
            print("                          %4s - %4s                             " % (coin1, coin2))
            print("_____________BIDS_____________ | _____________ASKS_____________")
            k=0
            for bid in KuBids:
                print("%3.6f" % float(bid[0]),space*4,"- %8.4f" %  float(bid[1]),space*7, " %3.6f" % float(KuAsks[k][0]), space*4, "-  %7.4f"  %   float(KuAsks[k][1]), flush=True)
                k += 1
            if trade_amt:
                expected_value = round(float(trade_amt / float(KuAsks[0][0])),12)
                print("\n", space*17, "Expected: %3.12f" % float(expected_value), flush=True)    
                minimum_value = round(float(trade_amt / float(KuAsks[-1][0])),12)
                print("\n", space*18, "Minimum: %3.12f" % float(minimum_value), flush=True)
            if target_amt and trade_amt:
                target_price = round(float(trade_amt / target_amt),12)
                print("\n", space*19, "Target: %3.12f" % float(target_price), flush=True)
            if target_amt and expected_value >= target_amt:
                while True:
                    call(['aplay', 'sounds/alarm.wav'])
                
        except:
            print("error reading JSON")
            

def main():
    parser = argparse.ArgumentParser(description="KuCoin - Order Books for Trading Pair")

    parser.add_argument('coins', metavar='coin', nargs='+')
    parser.add_argument('-a', '--amount', help="Enter Amount Wanting to Trade", metavar='amount')
    parser.add_argument('-t', '--target', help="Target Amount Wanting to Receive", metavar='target')
    args = parser.parse_args()
    
    coin1 = args.coins[0]
    coin2 = args.coins[1]
    
    get_kucoin_order_books(coin1, coin2, args)


if __name__ == "__main__":
    main()

