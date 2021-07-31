#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import pandas as pd
import swifter
import numpy as np
import time

def elapsed(f):
    def wrap(*args):
        start_r = time.perf_counter()
        start_p = time.process_time()
        ret = f(*args)
        end_r = time.perf_counter()
        end_p = time.process_time()
        elapsed_r = end_r - start_r
        elapsed_p = end_p - start_p
        print(f'{f.__name__} elapsed: {elapsed_r:.6f}sec (real) / {elapsed_p:.6f}sec (cpu)')
        return ret
    return wrap

@elapsed
def df_rand(row_size):
    df = pd.DataFrame(np.random.randint(0,row_size,size=(row_size, 1)), columns=['x'])

    # # 빈 DataFrame 생성하기
    # df = pd.DataFrame(columns=['idx', 'x'])
    # for idx in range(1, row_size):
    #     # 1과 size  사이의 random 한 값 생성하기
    #     number = random.randint(1, row_size)
    #     # DataFrame에 특정 정보를 이용하여 data 채우기
    #     df = df.append({'idx':idx, 'x':number}, ignore_index=True)
    # df.set_index('idx', inplace=True)
    return df

@elapsed
def run_singlecore(df):    
    # runs on single core
    df['x2'] = df['x'].apply(lambda x: x**2)

@elapsed
def run_multicore(df):
    # runs on multiple cores
    df['x2'] = df['x'].swifter.apply(lambda x: x**2)

    # use swifter apply on whole dataframe
    # df['agg'] = df.swifter.apply(lambda x: x.sum() - x.min())
    # use swifter apply on specific columns
    # df['outCol'] = df[['inCol1', 'inCol2']].swifter.apply(my_func)
    # df['outCol'] = df[['inCol1', 'inCol2', 'inCol3']].swifter.apply(my_func,positional_arg, keyword_arg=keyword_argval)

if __name__ == '__main__':
    df = df_rand(10000000+1)

    print ('\nn=100')
    df_sample = df.sample(n=100)
    run_singlecore(df_sample)
    run_multicore (df_sample)
 
    print ('\nn=1000')
    df_sample = df.sample(n=1000)
    run_singlecore(df_sample)
    run_multicore (df_sample)

    print ('\nn=10000')
    df_sample = df.sample(n=10000)
    run_singlecore(df_sample)
    run_multicore (df_sample)
 
    print ('\nn=100000')
    df_sample = df.sample(n=100000)
    run_singlecore(df_sample)
    run_multicore (df_sample)
 
    print ('\nn=1000000')
    df_sample = df.sample(n=1000000)
    run_singlecore(df_sample)
    run_multicore (df_sample)
 
    print ('\nn=10000000')
    df_sample = df.sample(n=10000000)
    run_singlecore(df_sample)
    run_multicore (df_sample)