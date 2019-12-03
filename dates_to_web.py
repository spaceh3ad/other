from selenium import webdriver
import csv, sys, time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidArgumentException

def open_links():
    # run in the current dir
    # take all links
    links = []
    with open('{}'.format(sys.argv[1])) as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for column in reader:
            links.append(column['links'])

    driver = webdriver.Chrome()
    for i in links:
        print(i)
        driver.get(i)
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[1])

try:
    open_links()
except InvalidArgumentException:
    print("Didn't open link")
finally:
    time.sleep(900000)
