# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 10:26:27 2022

@author: SHYAM SUNDER
"""

def update_day_stop_loss(day_stop_loss):
    open('stop_loss_day.txt', 'w').close()
    with open('stop_loss_day.txt', 'w') as f:
        f.write(day_stop_loss)


def update_max_stop_loss(max_stop_loss):
    open('stop_loss_max.txt', 'w').close()
    with open('stop_loss_max.txt', 'w') as f:
        f.write(max_stop_loss)