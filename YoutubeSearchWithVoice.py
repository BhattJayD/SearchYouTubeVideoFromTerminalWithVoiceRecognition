from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import speech_recognition as sr
import os

lan="en"
r=sr.Recognizer()
mic=sr.Microphone()
with mic as sour:
	r.adjust_for_ambient_noise(sour)
	print("Speak anything:- ")
	audio=r.listen(sour,timeout=5, phrase_time_limit=5)
try:
	teext=r.recognize_google(audio)
	print("you said:-",teext)
	print(t)
	with open("logs.txt","a") as f:
		f.write(f"{teext}\r\n")
except:
	pass
time.sleep(5)
driver = webdriver.Firefox()
driver.get('https://www.youtube.com/')
stri=teext
time.sleep(2)
search=driver.find_element_by_xpath('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
search.send_keys(teext)


#treanding=driver.find_element_by_xpath('/html/body/ytd-app/div/app-drawer/div[2]/div/div[2]/div[2]/ytd-guide-renderer/div[1]/ytd-guide-section-renderer[1]/div/ytd-guide-entry-renderer[2]/a/paper-item')
#treanding.click()
#chaina=driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-browse[2]/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[1]/div[2]/ytd-channel-list-sub-menu-renderer/div/ytd-channel-list-sub-menu-avatar-renderer[1]/a')
#chaina.click()
btn=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
btn.click()

#jay=driver.find_element_by_xpath('//*[@id="info"]')
#jay.click()
#new WebDriverWait(driver, 20).until(ExpectedConditions.elementToBeClickable(By.cssSelector("button.nsg-button"))).click();
