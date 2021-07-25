#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd

# csv file에서 읽기
#df = pd.read_csv('./Grade_sample.csv')
df = pd.read_csv('https://raw.githubusercontent.com/kibua20/devDocs/master/pandas_example/Grade_Sample.csv')
print (df)

# groupby()
df_groupby = df.groupby(['Grade']).mean()
print (type(df_groupby))
print ('GropyBy Result:')
print (df_groupby)