# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 08:13:25 2019

@author: Hamdan Ali
"""

import argparse

import pandas as pd

def read_data (fname):
    df=pd.read_csv(fname)
    mean= df['amount'].mean()
    describe =df['amount'].describe()
    sumx=df['amount'].sum()
    count_row=df['id'].count()
    head=df.head(100)
    last=df.tail(100)
    return ('MEAN:', mean,
            "DESCRIBE:", describe,
            "COUNT OF ROWS:", count_row,
            "SUM:", sumx,
            "100 DATA PERTAMA:", head,
            "100 DATA TERAKHIR:", last)
    
if __name__== "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-f","--file", type=str, required=True, help="Run Program")
    args=options.parse_args()
    data=read_data(args.file)
    print(data)