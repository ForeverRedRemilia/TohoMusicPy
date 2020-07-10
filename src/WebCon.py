import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def webconnect(music):
    url = "https://music.163.com/#/search/m/?s=\"" + music + "\"&type=1"
    options = Options()
    options.add_argument('--headless')
    # driver = webdriver.Firefox(executable_path='geckodriver', firefox_options=firefox_options)
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    # time.sleep(5)
    driver.switch_to.frame('g_iframe')
    time.sleep(1)
    each = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/em').text
    driver.close()
    return each
