from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def main():
    chromedriver_path = '/Users/ryan/Downloads/chromedriver'
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    browser = webdriver.Chrome(executable_path=chromedriver_path, chrome_options=option)
    # browser = webdriver.Chrome(executable_path=chromedriver_path)
    browser.implicitly_wait(5)
    browser.get("https://baidu.com")
    print(browser.title)
    search_box = browser.find_element(by=By.ID, value='kw')
    search_btn = browser.find_element(by=By.ID, value='su')
    search_box.send_keys("hello")
    search_btn.click()
    time.sleep(3)
    print(browser.title)


if __name__ == '__main__':
    main()
