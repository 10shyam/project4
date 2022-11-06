# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 00:22:31 2022

@author: SHYAM SUNDER
"""
from Generate_Session_File import Generate_Session
import logging

kite=Generate_Session()


def send_orders_buy(INSTRUMENT,QUANTITY):
    try:
        order_id = kite.place_order(tradingsymbol=INSTRUMENT,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=QUANTITY,
                                    variety=kite.VARIETY_AMO,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_CNC,
                                    validity=kite.VALIDITY_DAY)
    
        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))
        

def send_orders_sell(INSTRUMENT,QUANTITY):
    try:
        order_id = kite.place_order(tradingsymbol=INSTRUMENT,
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_SELL,
                                    quantity=QUANTITY,
                                    variety=kite.VARIETY_AMO,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_CNC,
                                    validity=kite.VALIDITY_DAY)
    
        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))

# Fetch all orders
kite.orders()