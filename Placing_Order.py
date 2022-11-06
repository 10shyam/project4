from Generate_Session_File import Generate_Session
import logging
def order_place():
    kite=Generate_Session()
 
    logging.basicConfig(level=logging.DEBUG)
    
    # Place an order
    try:
        order_id = kite.place_order(tradingsymbol="INFY",
                                    exchange=kite.EXCHANGE_NSE,
                                    transaction_type=kite.TRANSACTION_TYPE_BUY,
                                    quantity=1,
                                    variety=kite.VARIETY_AMO,
                                    order_type=kite.ORDER_TYPE_MARKET,
                                    product=kite.PRODUCT_CNC,
                                    validity=kite.VALIDITY_DAY)
    
        logging.info("Order placed. ID is: {}".format(order_id))
    except Exception as e:
        logging.info("Order placement failed: {}".format(e.message))


order_place()

