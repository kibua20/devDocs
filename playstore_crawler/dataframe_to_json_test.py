from numpyencoder import NumpyEncoder
import pandas as pd
import numpy as np 
import json

def add(a, b, c):
    return a + b + c
 
def test1():
    data = {'A':[1, 2, 3], 'B':[4, 5, 6],  'C':[7, 8, 9] }

    df = pd.DataFrame(data)
    dict_temp = dict()
    dict_temp['SUM'] = df['A'].sum()

    print (df)
    print (json.dumps(dict_temp, cls= NumpyEncoder, indent=4, ensure_ascii=False))
    print (json.dumps(dict_temp))

def test2():
    numpy_data = np.array([0, 1, 2, 3])
    print (type(numpy_data[0]))
    print (json.dumps(numpy_data, cls= NumpyEncoder))
    print (json.dumps(numpy_data))

def test3():
    data = {'A':[1, 2, 3],
        'B':[4, 5, 6],
        'C':[7, 8, 9] }
    
    df = pd.DataFrame(data)
    print(df, '\n')

    df['add'] = df.apply(lambda row : add(row['A'], row['B'], row['C']), axis = 1)
    df['mean'] = df.apply(np.mean, axis = 1)

    print('df.apply() axis=1')
    print(df,'\n')

    print(('df.apply() axis=0'))
    df2 = df.apply(np.sum, axis = 0)
    print(df2, '\n')

    print(('df.loc'))
    df.loc['Sum'] = df.apply(np.sum, axis = 0)
    print(df,'\n')
    
    print ('특정값 (B행, 1열):')
    print(df['B'][1],'\n')

    print(('df.transpose()'))
    df_tran = df.transpose()
    print(df_tran)


def add_multiply (a,b):
  return a+b, a*b

def test4():
    data = {'A':[1, 2, 3],
        'B':[4, 5, 6],
        'C':[7, 8, 9] }
    
    df = pd.DataFrame(data)
    print(df, '\n')
    
    df[['add', 'multiply']] = df.apply(lambda x: add_multiply(x['A'], x['B']), axis=1, result_type='expand')
    print(df, '\n')
    print (type(add_multiply(1,2)), add_multiply(1,2))
    
def test5():
    data = {'A':[1, 2, 3],
        'B':[4, 5, 6],
        'C':[7, 8, 9] }
    
    df = pd.DataFrame(data)
    print(df, '\n')
        
    df['add'], df['multiply'] = add_multiply(df['A'],df['B'])
    print(df, '\n')

def test6():
    # pandas.DataFrame.isin()은 두 날짜 사이에서DataFrame 행을 선택
    # pandas.Series.between()은 두 날짜 사이에서 DataFrame행을 선택
    # Bool mask를 선언하고 두 날짜 사이의 행을 pandas.DataFrame.loc(mask)으로 선택
    # pandas.DataFrame.query() 문으로 행을 선택   

    data = [
        ['2021-01-01', 1],
        ['2021-02-01', 2],
        ['2021-03-01', 3],
        ['2021-04-01', 4],
        ['2021-05-01', 5],
        ['2021-06-01', 6],
        ['2021-07-01', 7],
    ]    
    df = pd.DataFrame(data, columns=['Date', 'Value'])
    df['Date'] = pd.to_datetime(df['Date'])
    print (df.dtypes,'\n')
    print(df, '\n')
    
    df_filered =   df[ df['Date'].isin(pd.date_range('2021-02-01', '2021-05-01')) ]
    print (df_filered, '\n')
    
    df_filered =   df [df['Date'].between('2021-02-01', '2021-05-01')]
    print (df_filered, '\n')

    mask = (df['Date'] >= '2021-02-01') & (df['Date'] <= '2021-05-01')
    filtered = df.loc[mask]
    print (df_filered, '\n')

    # 날짜 열을 인덱스 열로 설정하여 통합df.loc[start_date : end_date]
    df = df.set_index(['Date'])
    filtered= df.loc['2021-02-01':'2021-05-01']
    print (df_filered, '\n')
    
    #query()
    filtered=df.query("Date >= '2021-02-01' and Date <='2021-05-01'")
    print (df_filered, '\n')
    
    #query() - 매주 월요일
    filtered2 = df.query('Date.dt.dayofweek == 0')
    print ('월요일인 경우:')
    print (filtered2, '\n')

    #query() - 5월인 경우
    query_month = 5
    filtered3 = df.query('Date.dt.month == @query_month')
    print ('5월인 경우:')
    print (filtered3, '\n')
   
if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    # test4()
    # test5()
    test6()