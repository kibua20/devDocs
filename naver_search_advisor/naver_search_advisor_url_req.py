#!/usr/bin/python3
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
import time

def naver_serach_advisor_url_req():
    #-----------------------------------------------------------------------
    # Naver Serach Advisor 의 ID 와 티스토리 마지막 포스팅 번호
    #your_id = 'kibua20'
    your_id = 'your_id'
    last_url = 60
    #------------------------------------------------------------------------

    blog_url = 'https://searchadvisor.naver.com/console/site/request/crawl?site=https%3A%2F%2F'+your_id+'.tistory.com'


    option = Options()
    profile_dir = os.path.join(os.getcwd(), 'profile')
    option.add_argument("user-data-dir="+profile_dir)
    option.set_capability('unhandledPromptBehavior', 'accept')

    # webdriver 얻어옴
    browser = webdriver.Chrome(options=option)

    # Naver 접속
    browser.get(blog_url)

    print ('Login first')

    # chrome에서 다운로드 완료 할때 까지 충분한 시간을 기다림
    time.sleep(30)

    print ('start')
    for idx in range(0,49):
        # 마지막 포스팅 번호에서 50개까지 입력
        url = str(last_url - idx)

        # text bod id가 변경됨
        try:
            element = browser.find_element_by_id("input-139")
        except:
            element = browser.find_element_by_id("input-202")
        
        # Text box 내용을 지움
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)

        # 티스토리 포스팅의 URL을 입력 
        element.send_keys(url)
        element.send_keys(Keys.TAB)
        time.sleep(0.1)
    
        # 등록 요청
        element.send_keys(Keys.ENTER)
        time.sleep(0.1)
        print ('URL 요청: ', url)

    browser.quit()
    print ('URL 입력 완료 및 브라우져 종료')


if __name__ == "__main__":
    naver_serach_advisor_url_req()
