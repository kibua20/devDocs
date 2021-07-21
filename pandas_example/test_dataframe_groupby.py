#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

# csv file에서 읽기
df = pd.read_csv('./Grade_sample.csv')
print (df)
df_groupby = df.groupby(['Grade']).mean()
print (df_groupby)