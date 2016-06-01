from gtts import gTTS
import pyperclip
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

driver = webdriver.Firefox()
decodeURL='http://ekantipur.com'
driver.get(decodeURL)


def speak(voicedata):
    print(voicedata)
    tts = gTTS(text=voicedata, lang='hi')
    tts.save("e:/hello.mp3")
    import winsound, sys
    import os
    os.system("start e:/hello.mp3")
    

# find the element that's name attribute
#textw = driver.find_element_by_class_name("display-news-title").text
speak(textw)



