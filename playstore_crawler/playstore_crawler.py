#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd


def playstore_crawler(url, ouputfile='./playstore_reviews.csv'):
    option = Options()
    option.add_argument("disable-infobars")
    option.add_argument("disable-extensions")
    #option.add_argument("start-maximized")
    option.add_argument('disable-gpu')
    option.add_argument('headless')


    # webdriver 얻어옴  - google-chrome --version으로  version을 확인하고 맞는 chrome drvier를 다운로드: https://chromedriver.chromium.org/downloads
    # webdriver
    try:
        browser = webdriver.Chrome('./chromedriver', options=option)
        print ('Load Chrome driver for Linux')
    except:
        browser = webdriver.Chrome('./chromedriver_mac', options=option)
        print ('Load Chrome driver for MacOS')
    
    browser.get(url)

    # scroll browser 
    SCROLL_PAUSE_TIME = 1
    SCROLL_MAX_NUM = 120
    last_height = browser.execute_script("return document.body.scrollHeight")
    loop = 0
    while loop < SCROLL_MAX_NUM :
        # scroll 
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        sleep(SCROLL_PAUSE_TIME) 
        
        # click 더보기
        try:
            browser.find_element_by_xpath("//span[@class='RveJvd snByac']").click() 
        except:
            pass
        
        # # break while loop 
        # new_height = browser.execute_script("return document.body.scrollHeight") 
        # if new_height == last_height: 
        #     break 
        # last_height = new_height

        loop = loop + 1

    html = browser.page_source

    # html find
    soup = BeautifulSoup(html,"html.parser")

    # get user div.bAhLNe.kx8XBd 
    users = soup.select('div.bAhLNe.kx8XBd > span')
    # print (len(users))
    # for u in users:
    #     print (u,  u.text)


    # # copy element
    # users = soup.select('span.X43Kjb')
    # print (len(users))
    # for u in users:
    #     print (u,  u.text)
    # browser.quit()
    # return


    # stars
    stars_string = soup.select('span.nt2C1d > .pf5lIe > div')
    stars = list()
    for s in stars_string:
        tmp = s['aria-label'].replace('별표 5개 만점에', '').replace('개를 받았습니다.', '')
        stars.append(tmp)

    # date 
    date = soup.select('div.bAhLNe.kx8XBd > div > span.p2TkOb')

    # likes :  div.jUL89d.y92BAb.K3ZHGe  aria-label
    likes = soup.find_all('div', {'aria-label':'이 리뷰가 유용하다는 평가를 받은 횟수입니다.'})

    # find short comments:  bN97Pc fbQN7e
    short_comments = soup.find_all('span',{'jsname':'bN97Pc'})

    #full comments 
    full_comments = soup.find_all('span',{'jsname':'fbQN7e'})

    # 상위 5개만 출력
    print ('Number of extracted Reviews =', len(users), len(stars), len(date), len(short_comments), len(full_comments))
    loop = 0
    for u, s, d, l, short_c, full_c  in zip (users, stars, date, likes, short_comments, full_comments):
        if (len(full_c.text) > 0):
            print (u.text,s, d.text, l.text, full_c.text)
        else:
            print (u.text,s, d.text, l.text, short_c.text)

        if (loop > 5):
            break
        loop = loop + 1

    # Save to CSV
    res_dict = list()
    for u, s, d, l, short_c, full_c  in zip (users, stars, date, likes, short_comments, full_comments):
        if (len(full_c.text) > 0):
            res_dict.append({ 
                'USER' : u.text,
                'STAR' : s, 
                'DATE' : d.text,
                'LIKE' : l.text, 
                'REVIEW' : full_c.text
            })
        else:
            res_dict.append({ 
                'USER' : u.text,
                'STAR' : s, 
                'DATE' : d.text,
                'LIKE' : l.text, 
                'REVIEW' : short_c.text
            })

    res_df = pd.DataFrame(res_dict) 
    res_df['DATE'] = pd.to_datetime(res_df['DATE'], format="%Y년 %m월 %d일")
    res_df.to_csv(ouputfile,index=False, encoding='utf-8-sig')

    browser.quit()

def main():
    # Google Player Store url
    url = 'https://play.google.com/store/apps/details?id=com.google.android.youtube&showAllReviews=true'
    playstore_crawler(url, 'com.google.android.youtube.csv')

if __name__ == '__main__':
    main()
