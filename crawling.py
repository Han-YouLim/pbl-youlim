from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import pywinauto

# Chrome의 경우 다운로드받은 chromedriver의 위치를 지정해준다.
browser = webdriver.Chrome('C:\\Users\\gksdb\\Desktop\\chromedriver.exe')
browser.get('https://vrew.voyagerx.com/ko/try/')

wait = WebDriverWait(browser, 4)
element = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'close')))
browser.find_element_by_class_name('close').click()
time.sleep(2)

# 파일 탭으로 이동
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[1]/div[1]/button[2]').click()
wait = WebDriverWait(browser, 15)

time.sleep(1)

# 새 영상 파일로 시작하기 버튼 클릭
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]').click()

# 파일 업로드
time.sleep(1)
path = 'F:\pro\pbl\codes\est1.mp4'
app = pywinauto.application.Application().connect(title_re='열기')
app.열기.Edit.SetText(path)
time.sleep(1)
app.열기.Button.click()
try:
    app.열기.Button.click()
except:
    pass

# 변환 확인
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'blue-button')))
browser.find_element_by_class_name('blue-button').click()       # blue-button : 확인 버튼
new_check = browser.find_elements_by_class_name('word')[:10]
time.sleep(30)

i = 0
check = browser.find_elements_by_class_name('word')[:10]
while check == new_check:
    new_check = browser.find_elements_by_class_name('word')[:10]
    print(i * 30, ' 초째아직 추출중')
    i += 1
    time.sleep(30)

# 파일 탭에서 추출 누르기, 전체화면이어야 함
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[1]/div[1]/button[2]').click()                          # 파일 탭으로 이동
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/div[10]').click()                     # 다른 형식으로 내보내기 클릭
browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div[1]/div[2]/div[2]/div[1]/ul/li[2]/div/button').click()         # 텍스트 클릭
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[6]/div[2]/div/div[2]/span').click()            # 타임스탭프 변환 박스 클릭
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[6]/div[2]/div[2]/div[2]').click()              # 타임스탬프 선택
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[7]/div[2]/div/div[2]/span').click()         # 줄바꿈 박스 클릭
browser.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[7]/div[2]/div[2]/div[2]').click()           # 줄바꿈 한번 클릭
browser.find_element_by_class_name('blue-button').click()
print('추출완료')
time.sleep(10)
