from kiteconnect import KiteConnect

def Generate_Session():
    from Access_Token import access_token_return,api_key_return     
    kite = KiteConnect(api_key=api_key_return())

    kite.set_access_token(access_token_return())
    return kite
