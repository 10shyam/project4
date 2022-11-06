# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 01:16:43 2022

@author: SHYAM SUNDER
"""



def fetch_day_stop_loss():
    with open('stop_loss_day.txt', 'r') as f:
        stop_loss_day=f.read()
    return stop_loss_day   


def fetch_max_stop_loss():
    with open('stop_loss_max.txt', 'r') as f:
        stop_loss_max=f.read()
    return stop_loss_max