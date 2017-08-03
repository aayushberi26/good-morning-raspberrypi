from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def request_birthdays(link, email, password):
    try:
        birthdays = []
        driver = webdriver.Chrome()
        driver.get(link)
        driver.find_element_by_id('email').send_keys(email)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginbutton').click()
        # wait until page loaded
        todays_birthdays_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_fbBirthdays__todayCard'))
            )
        todays_birthdays_pro_pics = todays_birthdays_div.find_elements_by_tag_name('img')
        for pro_pic in todays_birthdays_pro_pics:
            birthdays.append(pro_pic.get_attribute('aria-label'))
        response = 'Birthdays: '
        for birthday in birthdays:
            response += birthday + ', '
        return response[:-2]
    # if element not found, means there are no birthdays
    except:
        return 'No birthdays found'