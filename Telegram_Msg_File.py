import requests




def telegram_bot_sendtext(bot_message):

   bot_token = '5514395922:AAE31akNKsZ1GnlV10QPM9lmzo0M8WSTBRQ'
   bot_chatID = '-1001703229995'
   image = '/Total_M2M_Image.png'
   send_text  = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
   print(send_text)

   send_image ='https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message +'&photo=' + image 

   response = requests.get(send_image)

   #telegram_msg = requests.get(f'https://api.telegram.org/bot{bot_token}/sendPhoto?chat_id=bot_chatID&caption={msg}&photo={img_uri}')
   #print(telegram_msg)

   return response.json()


