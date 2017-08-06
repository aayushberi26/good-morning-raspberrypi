from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from birthday_credentials import (
    email,
    password,
    output_path
)

def request_birthdays():
    link = 'https://www.facebook.com/events/birthdays/'
    try:
        driver = webdriver.PhantomJS()
        driver.maximize_window()
        driver.get(link)
        driver.find_element_by_id('email').send_keys(email)
        driver.find_element_by_id('pass').send_keys(password)
        driver.find_element_by_id('loginbutton').click()
        # wait until page loaded
        todays_birthdays_div = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, '_fbBirthdays__todayCard'))
            )
        todays_birthdays_pro_pics = todays_birthdays_div.find_elements_by_tag_name('img')
        response = 'Birthdays: '
        for pro_pic in todays_birthdays_pro_pics:
            response += pro_pic.get_attribute('aria-label') + ', '
        response = '"' + response[:-2] + '"'
    # if element not found, means there are no birthdays
    except:
        response = "'Birthdays: None'"
    output = open(output_path + 'birthday_output.py', 'w')
    output.write('birthdays = ' + response)
    output.close()

if __name__ == '__main__':
    request_birthdays()
