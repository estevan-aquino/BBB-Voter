import json
import time
import random

from binascii import a2b_base64
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote import switch_to
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


def read_configuration_file():
    with open('config.json') as file:
        arguments = json.load(file)
    return arguments

def login(driver, email, password):
    driver.get('https://login.globo.com/login/6694?url=' + arguments['pollURL'])
    
    email_input = driver.find_element_by_name('login')
    password_input = driver.find_element_by_name('password')
    form = driver.find_element_by_id('login-form')

    email_input.send_keys(email)
    password_input.send_keys(password)
    form.submit()

def click_on_target(driver, target):
    driver.find_elements_by_class_name('HkYyhPWbPFN45MEcUG6p8')[target - 1].click()
    #driver.find_elements_by_class_name('ubPdW-GSZSydRXrbM3Ijz')[target - 1].click()


def click_on_captcha(driver):
    try:
        captcha_name = get_captcha_name(driver)
        captcha_src = driver.find_element_by_class_name('gc__3_EfD').get_attribute("src")
        data = captcha_src.split(';base64,')[1]
        binary_data = a2b_base64(data)

        filename = captcha_name + '_' + str(random.randint(1, 1000)) + '.png'

        fd = open('captchas/' + filename, 'wb')
        fd.write(binary_data)
        fd.close()
        #driver.find_element_by_class_name('gc__3_EfD').click()
        driver.find_element_by_class_name('gc__1JSqe').click() # clicar pra recarregar o captcha
    except:
        print('Element is not displayed, captcha is too slow')
        
def click_on_voteagain(driver):
    driver.find_element_by_class_name('_3cp810UG2oJrLjwD0iAIT4').click()
    
def get_captcha_name(driver):
    captcha_name = driver.find_elements_by_class_name('gc__2e8f-')
    return captcha_name[0].text
    

arguments = read_configuration_file()

print("You're voting on", arguments['targetPosition'])

driver = webdriver.Firefox(executable_path=arguments['webDriverPath'])
driver.implicitly_wait(8)

login(driver, arguments['credentials']['username'],
      arguments['credentials']['password'])

# Tempo de espera do login...
time.sleep(30)
#driver.get(arguments['pollURL'])

correct_votes = 0
while True:
    try:
        click_on_target(driver, arguments['targetPosition'])
        click_on_captcha(driver)
        time.sleep(5)
    except:
        print('Waiting back to the vote page')
    if not driver.find_element_by_class_name('_2ZXTvG5Di8A1hVo6BPQF_').is_displayed():
        click_on_captcha(driver)
        time.sleep(5)
    else:
        correct_votes += 1
        print('Success', correct_votes, 'computed')
        #driver.get(arguments['pollURL'])
        click_on_voteagain(driver)
    time.sleep(5)
driver.close()
