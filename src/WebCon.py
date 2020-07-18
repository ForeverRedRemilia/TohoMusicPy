def webconnect(music, driver):
    url = "https://thwiki.cc/" + music
    # driver = webdriver.Firefox(executable_path='geckodriver', firefox_options=firefox_options)
    driver.get(url)
    # time.sleep(5)
    # driver.switch_to.frame('g_iframe')
    each = driver.find_element_by_xpath("//span[@id='二次同人数据']/../following-sibling::table[1]/tbody/tr[6]/td[2]").text
    # driver.close()
    return each
