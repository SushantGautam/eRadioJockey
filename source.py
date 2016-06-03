from gtts import gTTS
import pyperclip
import os, shutil
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import winsound, sys

print("eRadioJockey Project")
print("___________________")
print("Dynamic Radio/ Paper Reader Project for LOCUS 2016.")
print("Contact 072bct544@ioe.edu.np if you wish to contribute.")
print("Checkout : https://github.com/SushantGautam/eRadioJockey")
print("\nNote:\nInternet Connection & Mozilla Firefox required!\nVLC path defined in the program.\n")
print("___________________")
print("\nLoading eKantipur website in Mozilla Firefox... . ")


driver = webdriver.Firefox()
decodeURL='http://ekantipur.com'
driver.get(decodeURL)

def speak(voicedata, num):
    print(str(num))
    tts = gTTS(text=voicedata, lang='hi')
    tts.save("e:/temp/"+str(num)+".mp3")
       

#find the element that's name attribute
textw = driver.find_elements_by_class_name("display-news-title")

x=1
while x <= 6 :
    speak(textw[x].text, x)
    x += 1
    
print("\nNow queuing the data to VLC media Player and quiting. . .")
os.system("c:/progra~2/VideoLAN/VLC/vlc.exe --started-from-file --playlist-enqueue e:/temp")

time.sleep(3)


