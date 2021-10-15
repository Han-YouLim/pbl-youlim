from threading import Thread

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pywinauto

# Chrome의 경우 다운로드받은 chromedriver의 위치를 지정해준다.
browser = webdriver.Chrome('F:\\pro\\pbl\\chromedriver.exe')
browser.get('https://console.ncloud.com/nest/domain')


# 네이버 클라우드 로그인
browser.find_element_by_name('username').send_keys(uid) #이메일
browser.find_element_by_name('passwordPlain').send_keys(upw) #비밀번호
browser.find_element_by_xpath('//*[@id="loginForm"]/button').click()
time.sleep(2)

# 클로바 빌더 실행
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[2]/table/tbody/tr/td[6]/button').click()
time.sleep(5)

# 인식 작업 요청 누르기
wait = WebDriverWait(browser, 60)
wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]')))
browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[2]/div[1]/div[1]/button[1]').click()

# 파일 업로드 클릭
browser.find_element_by_xpath('/html/body/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/ul/li[2]/a').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="dropzone"]/div').click()        # 업로드 박스 클릭

#파일 업로드 실행
time.sleep(1)
path = 'F:\pro\pbl-sample\sample1.m4a'
app = pywinauto.application.Application().connect(title_re='열기')
app.열기.Edit.SetText(path)
time.sleep(1)
app.열기.Button.click()
try:
    app.열기.Button.click()
except:
    pass
