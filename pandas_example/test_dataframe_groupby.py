#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd

def filter_func(df, x):
    #print (x['Test1'].mean)
    return df['Test1'] < x

# csv file에서 읽기
#df = pd.read_csv('./Grade_sample.csv')
df = pd.read_csv('https://raw.githubusercontent.com/kibua20/devDocs/master/pandas_example/Grade_Sample.csv')
#print (df)

# groupby()
df_groupby = df.groupby(['Grade']).mean()
#print (type(df_groupby))
#print ('GropyBy Result:')
#print (df_groupby)


# df_filter = df.groupby(['Grade'])
# #print (df_filter)
# df_filter = df.groupby(['Grade']).filter(lambda x: x['Grade'].mean() > 3)
# print (df_filter)
