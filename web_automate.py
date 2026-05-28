#for opening chrome and auto scrolling of youtube
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome() #used to open chrome
sleep(3)
browser.get("https://youtube.com")  
sleep(3)

input_box = browser.find_element("name","search_query")
input_box.send_keys("github")
sleep(3)

input_box.send_keys(Keys.ENTER)
sleep(30)
first_short = browser.find_element("xpath",'//*[@id="contents"]/grid-shelf-view-model[1]/div[1]/div[1]/div[1]/ytm-shorts-lockup-view-model-v2')
first_short.click()

while True:
    sleep(15)
    next_button = browser.find_element("xpath",'//*[@id="navigation-button-down"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div[2]')
    next_button.click()




