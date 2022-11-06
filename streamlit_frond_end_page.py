# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 00:56:47 2022

@author: SHYAM SUNDER
"""

import streamlit as st
from stop_loss_fetch import fetch_day_stop_loss, fetch_max_stop_loss
from update_stop_loss import update_day_stop_loss,update_max_stop_loss
from Calculate_Total_M2M_File import update_positions_table,Calculate_Total_M2M
from Generate_Session_File import Generate_Session
from Telegram_Msg_File import telegram_bot_sendtext
st.set_page_config(page_title='Shamili Website')
import pandas as pd
from exit_all_orders import exit_all_positions
from  data_frame_testing import data_frame_test
from Sending_M2M_Based_Alerts import sending_alerts
import time

#df1 = pd.read_excel('positions.xlsx', sheet_name = 1)

st.header('Shamili Trade Analysis')
st.subheader('Current Positions')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.text("")
    if st.button("Fetch Day Stop Loss"):
        f1=fetch_day_stop_loss()
        st.write('day stop loss is : %s' % f1)
        
    if st.button("Fetch max Stop Loss"):
        f2=fetch_max_stop_loss()
        st.write('max stop loss is : %s' % f2)


kite=Generate_Session()
positions=kite.positions()

df1=update_positions_table(positions)                                                                                                                                                                                             


Total_M2M=Calculate_Total_M2M(positions)
    
with col2:
    day_stop_loss=fetch_day_stop_loss()
    updated_day_stop_loss = st.text_input('Update day Stoploss', day_stop_loss)
    if st.button("Update Day Stop Loss",):
        update_day_stop_loss(updated_day_stop_loss)
        st.write('Day Stop Loss is updated as : %s' % updated_day_stop_loss)
        telegram_bot_sendtext("Day Stop Loss is updated as :" + updated_day_stop_loss)
    

with col3:   
    max_stop_loss=fetch_max_stop_loss()
    updated_max_stop_loss = st.text_input('Update  max Stoploss', max_stop_loss)
    if st.button("Update Max Stop Loss",):
        update_max_stop_loss(updated_max_stop_loss)
        st.write('Max Stop Loss is updated as : %s' % updated_max_stop_loss)
        telegram_bot_sendtext("Max Stop Loss is updated as :" + updated_max_stop_loss)
    
with col4:
    
    if st.button("Exit all"):
        exit_all_positions(df1)
        telegram_bot_sendtext("Exit all is initiated ")
        


if st.button("Push Alerts"):
    sending_alerts(kite,-10000)

col1, col2, col3, col4, col5 = st.columns(5)

with col4:

    st.metric(label="Total M2M", value=Total_M2M)

st.dataframe(df1)


while True:
     # update every 5 mins
     Total_M2M=Calculate_Total_M2M(positions)
     sending_alerts(kite,-20000)
     
     for x in range(1, 60, 1):
         if(x>58):
             telegram_bot_sendtext("program is running fine")
         time.sleep(10)
         
     
     
