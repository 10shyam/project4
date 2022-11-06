from Telegram_Msg_File import telegram_bot_sendtext
from Calculate_Total_M2M_File import Calculate_Total_M2M,update_TotalM2M_Image
from Send_image import send_photo_telegram


def sending_alerts(kite,M2M_alert_Limit):    

    positions=kite.positions()

    Total_M2M=Calculate_Total_M2M(positions)
    update_TotalM2M_Image(positions)

    if(Total_M2M<M2M_alert_Limit*-1):
        
        telegram_bot_sendtext("P/L is Rs. "+ str(Total_M2M))
        send_photo_telegram()

