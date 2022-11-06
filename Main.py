# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:45:43 2022

@author: SHYAM SUNDER
"""

from Generate_Session_File import Generate_Session
from Sending_M2M_Based_Alerts import sending_alerts
from exit_all_orders import exit_all_positions

exit_all_SL=5


kite=Generate_Session()
sending_alerts(kite,20000,1)

exit_all_positions(exit_all_SL)

