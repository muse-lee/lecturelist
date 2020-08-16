from selenium import webdriver
import time

driver = webdriver.Chrome('/Users/ATIV9/Desktop/coding/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://oc30.ebssw.kr/sso/loginView.do?loginType=onlineClass')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('j_username').send_keys('eyedimuse')
driver.find_element_by_name('j_password').send_keys('muselee103^^')
# 로그인 버튼을 눌러주자.
driver.find_element_by_xpath('//*[@id="loginViewForm"]/div/div[1]/fieldset/div/button').click()

time.sleep(2)

obj = driver.switch_to.alert
obj.accept()

time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[1]/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[1]/div/ul/li[2]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[2]/div/ul/li[6]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[3]/div/ul/li[3]').click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[4]/div').click()
driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[4]/div/ul/li[8]').click()
time.sleep(2)


driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div/div/div/div/div[2]/div[5]/a').click()
time.sleep(3)

driver.get('')


