Access_token_value=''


def access_token_store(access_token_var):
    open('access_token_file.txt', 'w').close()
    with open('access_token_file.txt', 'w') as f:
        f.write(access_token_var)
    
    
def access_token_return():
    with open('access_token_file.txt', 'r') as f:
        access_token=f.read()
    return access_token

def api_key_return():
    with open('api_key_file.txt', 'r') as f:
        api_key_var=f.read()
    return api_key_var