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
   
if __name__ == '__main__':
    # test1()
    # test2()
    # test3()
    test4()