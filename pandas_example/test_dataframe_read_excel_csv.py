#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import pandas as pd

# excel 파일 읽기
df1 = pd.read_excel('./Grade_Sample.xlsx', sheet_name='Sheet1')

# url에서 excel 읽기
df = pd.read_excel('https://raw.githubusercontent.com/kibua20/devDocs/master/pandas_example/Grade_Sample.xlsx')
print (type(df))
print (df)

# csv file에서 읽기
df = pd.read_csv('./copy_grade_sample.csv')

# url에서 csv 읽기
df = pd.read_csv('https://raw.githubusercontent.com/kibua20/devDocs/master/pandas_example/Grade_Sample.csv')

# csv file로 저장
print ('Write to csv')
df.to_csv('copy_grade_sample.csv', index=False, encoding='utf-8-sig')

