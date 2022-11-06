# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 23:03:22 2022

@author: SHYAM SUNDER
"""
from send_orders import send_orders_buy,send_orders_sell

def exit_all_positions(df):

    for x in range(1):
        print("Iteration"+ str(x))
        buy_quantity=0
        sell_quantity=40
        tradingsymbol=df['tradingsymbol'][1]
        print(tradingsymbol)
        if(sell_quantity>buy_quantity):
            Buy_Quantity=sell_quantity-buy_quantity
            send_orders_buy(df['tradingsymbol'][1],Buy_Quantity)   
            
        if(buy_quantity>sell_quantity):
            Sell_Quantity=buy_quantity-sell_quantity
            send_orders_sell(['tradingsymbol'][1],Sell_Quantity)                
