#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

print ('read_excel()\n')
df = pd.read_excel('./Grade_Sample.xlsx')
print (df)


df = pd.read_csv('./Grade_Sample.csv')
print ('read_csv()')
print(df)

