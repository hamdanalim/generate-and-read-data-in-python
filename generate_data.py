# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 13:26:50 2019

@author: Hamdan Ali
"""


import pandas as pd
import numpy as np
import datetime
import uuid
from random import randrange
import csv

dft = pd.DataFrame({'id' : [uuid.uuid4() for i in range(4800000)],
                    'device_id' : ['00010','00011','00012','00013','00014','00015','00016','00017',
                                   '00018','00019','0001A','0001B','0001C','0001D','0001E','0001F'] * 300000,
                   'username' : ['Andi', 'Budi', 'Taja'] * 1600000,
                   'lokasi' : ['Bandung', 'Jakarta'] * 2400000,
                    'amount' : [np.random.randint(10, 1000) for i in range(4800000)],
                    'timestamp' : [np.random.choice(pd.date_range(datetime.datetime(2019,1,1),datetime.datetime(2019,12,30))) for i in range(4800000)] 
                    #'time' : [[date.strftime('%H:%M:%S') for date in pd.date_range(start='2017-01-01', end='2017-01-04', periode=120)]]
                   })
dft.to_csv('dft2.txt', index=False)
