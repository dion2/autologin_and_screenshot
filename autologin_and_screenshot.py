import time
import numpy as np
from PIL import ImageGrab
from selenium import webdriver
from datetime import datetime as dt

# 使用 Chrome 的 WebDriver
browser = webdriver.Chrome()
# chrome 參數加入
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
# options.add_argument("--test-type")
options.add_argument("--start-maximized")
# options.binary_location = "/usr/bin/chromium"
browser = webdriver.Chrome(chrome_options=options)
browser.get('http://127.0.0.1/d-crm/login/login.php')
# 輸入帳號
elem_user = browser.find_element_by_name("account")
elem_user.clear
elem_user.send_keys("Username")  
# 輸入密碼
elem_password = browser.find_element_by_name("password")
elem_password.clear
elem_password.send_keys("Password")  
browser.find_element_by_id("btn-submit").submit()
# 暫停幾秒讓登入存取時間
time.sleep(15)  
# 拍攝全螢幕
im = ImageGrab.grab()
# 時間點為檔名
im.save( dt.now().strftime('%Y%m%d%H%M%S') + '.png')
browser.close()
browser.quit()
