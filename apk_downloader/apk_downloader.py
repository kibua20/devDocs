#!/usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import time

def main():
    apklist = [
            'com.android.vending', 
            'com.google.android.apps.docs.editors.docs',
            'com.google.android.apps.youtube.music', 
            'com.google.android.videos'
            ]

    apk_download (apklist) 

def apk_download(apklist):
    option = Options()
    option.add_argument("disable-infobars")
    option.add_argument("disable-extensions")
    #option.add_argument("start-maximized")
    option.add_argument('disable-gpu')
    option.add_argument('headless')
    option.add_argument("user-data-dir=./profile")

    option.add_experimental_option("prefs", {
        "download.default_directory": r"./download",
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    browser = webdriver.Chrome(options=option)

    # apk list 에서 apk download 시도함 
    for apk in apklist:
        apk_mirror_url = 'https://m.apkpure.com/kr/google-play-store/{}/download?from=details'.format(apk)
        print ('Download apk', apk)
        browser.get(apk_mirror_url)
        time.sleep(10)

    # chrome에서 다운로드 완료 할때까지 충분한 시간을 기다림
    time.sleep(30*10)

    # chrome 종료
    browser.quit()
    print ('Finish')


if __name__ == "__main__":
    main()
