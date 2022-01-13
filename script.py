from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from playsound import playsound



driver = webdriver.Firefox(executable_path=r'geckodriver.exe')
driver.get('https://registrar.kfupm.edu.sa/courses-classes/course-offering/')

termSelect = Select(driver.find_element_by_id('course_term_code')).select_by_index(2)
depSelect = Select(driver.find_element_by_id('course_dept_code'))

i = 0
for item in depSelect.options:
    print(str(i)+' - '+item.get_attribute('innerText'), item.get_attribute('value'))
    i=i+1

department = input("Enter the dpartment index: ")
depSelect.select_by_index(department)

courseCRN = int(input('Enter the course CRN: '))


while (True):
    section_Open_Or_Closed= driver.find_element_by_xpath(f"//*[contains(text(), '{courseCRN}')]/following-sibling::td[6]")
    waitlist_Open_Or_Closed= driver.find_element_by_xpath(f"//*[contains(text(), '{courseCRN}')]/following-sibling::td[7]")
    if section_Open_Or_Closed.text == 'Closed' and waitlist_Open_Or_Closed.text == 'Closed':
        print("section is closed")
        time.sleep(1)
        driver.execute_script("course_api()")
        time.sleep(1)
    else:
        for i in range(20):
            playsound('sound.wav')
        break


