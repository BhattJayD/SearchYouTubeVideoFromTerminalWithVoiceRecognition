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

btn=driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
btn.click()

#jay=driver.find_element_by_xpath('//*[@id="info"]')
#jay.click()
#new WebDriverWait(driver, 20).until(ExpectedConditions.elementToBeClickable(By.cssSelector("button.nsg-button"))).click();
