#!/usr/bin/python3
# -*- coding: utf-8 -*-


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import os
import time

#파이썬 Selenium을 활용한 블서치 백링크 등록 자동화 - https://kibua20.tistory.com/103
def blogsearch_kr_url_req():
    #---------------------------------------------------------------------------------------------------
    # 티스토리 ID     e.g.) https://kibua20.tistory.com/ 인 경우 kibua20 설정
    # blog_id = 'kibua20'
    blog_id = 'your_id'

    # 로그 포스팅의 시작과 끝 번호 -  https://kibua20.tistory.com/2   ~ https://kibua20.tistory.com/102 
    from_url =2
    to_url = 102
    #-----------------------------------------------------------------------------------------------------

    blog_url = 'https://'+ blog_id+ '.tistory.com/'

    # 블로그 서치 티스토리 등록 URL
    blogsearch_url = 'https://blogsearch.kr/tistory'

    option = Options()
    profile_dir = os.path.join(os.getcwd(), 'profile')
    option.add_argument("user-data-dir="+profile_dir)

    option.add_argument("disable-infobars")
    option.add_argument("disable-extensions")
    option.set_capability('unhandledPromptBehavior', 'accept')

    # webdriver 얻어옴
    browser = webdriver.Chrome(options=option)

    # blogsearch_url 접속
    browser.get(blogsearch_url)    
    for idx in range(from_url,to_url+1):
        url = blog_url + str(idx)
        print(url)
        element = browser.find_element_by_class_name('form-control')

        # clear keys and url strings
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        element.send_keys(url)

        # 등록 버튼 clk
        element_btn = browser.find_element_by_class_name('btn-dark')
        element_btn.click()

        try:
            time.sleep(1)
            browser.switch_to.alert.accept()
        except:
            time.sleep(0.5)
            pass

    time.sleep(2)
    browser.quit()

if __name__ == "__main__":
    blogsearch_kr_url_req()
