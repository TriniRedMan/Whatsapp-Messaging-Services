







# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 15:24:33 2022

@author: Sandrine
"""

import pyautogui as pg
import webbrowser as web
import time
import pandas as pd
from tkinter import *

win = Tk() # Some Tkinter stuff

screen_width = win.winfo_screenwidth() # Gets the resolution (width) of your monitor
screen_height= win.winfo_screenheight() # Gets the resolution (height) of your monitor

print(screen_width, screen_height) # prints your monitor's resolution

my_file = open("sample.txt", "r")
content_list = my_file.readlines()

print(content_list[0])
print(content_list[1])

screen_height =content_list[0]
screen_width =content_list[1]

screen_height = int(screen_height)
screen_width =int(screen_width
                  
                  
                  )



data = pd.read_csv("leads.csv",encoding_errors='ignore')
#data = pd.read_csv("leads.csv",encoding='unicode_escape')
data['int'] = 0
data_dict = data.to_dict('list')
leads = data_dict['LeadNumber']
messages = data_dict['Message']
combo = zip(leads,messages)
first = True
for lead,message in combo:
    
    
    
    time.sleep(1)
    print(lead)
    print(type(lead))
    lead = int(lead)
    lead = str(lead)
    print(type(lead))
    web.open("https://web.whatsapp.com/send?phone="+lead+"&text="+message)
    pg.press('enter')
    
    #web.open("https://web.whatsapp.com/send?phone="+"&text="+message)
    if first:
        time.sleep(5)
        first=False
        
    time.sleep(5)
    
    
    
    
    width,height = pg.size()
    #pg.click(width/2,height/2)
    #time.sleep(1)
    
    

   # pg.press('enter')
    
    time.sleep(5
               
               )
    
    #pg.moveTo(screen_width * 0.694, screen_height* 0.964) # Moves the cursor the the message bar in Whatsapp
    pg.moveTo(screen_width * 1, screen_height* 1)
    
    pg.click() # Clicks the bar
    time.sleep(2)
    
    
    #
    pg.press('enter') 
    
    time.sleep(1)
    pg.hotkey('ctrl', 'w')