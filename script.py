from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from playsound import playsound



driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://registrar.kfupm.edu.sa/courses-classes/course-offering/')
termSelect = Select(driver.find_element_by_id('course_term_code')).select_by_index(2)
depSelect = Select(driver.find_element_by_id('course_dept_code')).select_by_index(19)


courseCRN = int(input('Enter the course CRN: '))
# print("hello {courseCRN}")
# time.sleep(1)


while (True):
    section_Open_Or_Closed= driver.find_element_by_xpath(f"//*[contains(text(), '{courseCRN}')]/following-sibling::td[6]")
    waitlist_Open_Or_Closed= driver.find_element_by_xpath(f"//*[contains(text(), '{courseCRN}')]/following-sibling::td[7]")
    if section_Open_Or_Closed.text == 'Closed' and waitlist_Open_Or_Closed.text == 'Closed':
        print("section is closed")
        time.sleep(1)
        driver.execute_script("course_api()")
        time.sleep(1)


    else:
        playsound('sound.wav')
        break












# openOrClose= driver.find_element_by_xpath("//*[contains(text(), '{courseCRN}')]")

# print(openOrClose.text)


# /html/body/section[2]/div/div/div/div[2]/table/tbody/tr[3]/td[3]


# /html/body/section[2]/div/div/div/div[2]/table/tbody/tr[3]/td[9]/span


# stringButtonForRefresh = "course_api()"
# driver.execute_script(stringButtonForRefresh)