# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:12:38 2019

@author: Administrator
"""




       
def hour_minute_meet():
    for i in range(1,12):
        meet_time=i*60/(minute_hand_velo-hour_hand_velo)
        print(time.strftime("%H:%M:%S", time.gmtime(meet_time)))
               

import time   
        
if __name__=='__main__':
    
    second_hand_velo=1        
    minute_hand_velo=1/60
    hour_hand_velo=1/60/12
    hour_minute_meet()

