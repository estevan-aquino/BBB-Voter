import json
import time

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
    driver.get('https://login.globo.com/login/4728')
    
    email_input = driver.find_element_by_name('login')
    password_input = driver.find_element_by_name('password')
    form = driver.find_element_by_id('login-form')

    email_input.send_keys(email)
    password_input.send_keys(password)
    form.submit()

def click_on_target(driver, target):
    driver.find_elements_by_class_name('HkYyhPWbPFN45MEcUG6p8')[target - 1].click()


def click_on_captcha(driver):
    time.sleep(2)
    driver.find_element_by_class_name('gc__3_EfD').click()

def clickar_votardnv(driver):
    time.sleep(2)
    driver.find_element_by_class_name('_3viry_vXUhTU4nSnvn2iB_').click()
    

arguments = read_configuration_file()

print("You're voting on", arguments['targetPosition'])

driver = webdriver.Firefox(executable_path=arguments['webDriverPath'])
driver.implicitly_wait(8)

login(driver, arguments['credentials']['username'],
      arguments['credentials']['password'])

time.sleep(5)
driver.get(arguments['pollURL'])

correct_votes = 0
while True:

    time.sleep(3)
    click_on_target(driver, arguments['targetPosition'])
    print('---Abriu o Conteiner---')

    try:
        while not driver.find_element_by_class_name('_3viry_vXUhTU4nSnvn2iB_').is_displayed():    
            click_on_captcha(driver)
            print('*Clicou no Captcha*')
            time.sleep(3)

        correct_votes += 1
        print(correct_votes, 'computed')
        # driver.get(arguments['pollURL']) --- descontinuado
        clickar_votardnv(driver)
        print('Reset Page')
        time.sleep(3)
    except:
        print("Ocorreu algum erro! Resetando Página")
        driver.close()
        print('Reseting Program...')
        time.sleep(3)

        driver = webdriver.Firefox(executable_path=arguments['webDriverPath'])
        driver.implicitly_wait(5)
        print("Done!")
        login(driver, arguments['credentials']['username'],
        arguments['credentials']['password'])
        time.sleep(4)
        print("Logado!")
        driver.get(arguments['pollURL'])
        print("Acessando site de votação...")

    

print('Saiu do Loop por algum motivo')
driver.close()