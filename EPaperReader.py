from gtts import gTTS
import shutil
import time, os, glob
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import winsound, sys
from datetime import datetime
import urllib
import subprocess

import winsound, sys

os.system('taskkill /f /im vlc.exe')
os.system('cls')

print("NewsPaper Reader- eRadioJockey Project")
print("___________________")
print("Dynamic Radio/ Paper Reader Project for LOCUS 2016.")
print("Contact 072bct544@ioe.edu.np if you wish to contribute.")
print("Checkout : https://github.com/SushantGautam/eRadioJockey")
print("\nNote:\nInternet Connection required!\nVLC path defined in the program.\n")
print("___________________")
print("\nCooking news for you. . . ")


driver = webdriver.Firefox()
#driver = webdriver.PhantomJS(executable_path="E:\Twister/BackEnd/twisterBackEng.exe", service_args=['--load-images=no'])
#ekantipur.com
#driver.addAdditionalPreference("general.useragent.override", " Nokia Symbian - Nokia5250/10.0.011 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Safari/525 3gpp-gba ")
#decodeURL='http://googleweblight.com/?lite_url=http://kathmandupost.ekantipur.com/'
global decodeURL
decodeURL ='http://googleweblight.com/?lite_url=http://ekantipur.com'

def scrapandPlay(url):
    os.system('taskkill /f /im vlc.exe')
    driver.get(url)
    test = 'E:\SandBox\Python\eradioJockey\\temp\\*'
    r = glob.glob(test)
    for i in r:
       os.remove(i)

    def speak(voicedata, num):
        tts = gTTS(text=voicedata, lang='hi')
        tts.save("E:\SandBox\Python\eradioJockey/temp/eNews.mp3")
           
    #find the element that's name attribute class_name display-news-title

    textw = None
    while not textw:
    	try:
        	textw = driver.find_element_by_class_name('content-wrapper')
    	except NoSuchElementException:
        	time.sleep(0)

    
    speak(textw.text, 0)
    
    #os.system("c:/progra~2/VideoLAN/VLC/vlc.exe E:\SandBox\Python\eradioJockey\\temp\\eNews.mp3")
 
    print("\nServing via VLC media player (WIN64). . .")
    subprocess.Popen("c:/progra~2/VideoLAN/VLC/vlc.exe -I null E:\SandBox\Python\eradioJockey\\temp\\eNews.mp3", shell=True, stdin=None, stdout=None, stderr=None, close_fds=True)
    
    
    while driver.current_url == url:
    	print '1'

    decodeURL = driver.current_url	
    print("Cooking. . ")

    try:
		scrapandPlay(driver.current_url)
    except :
		print("Nothing to read. . . ")

	


scrapandPlay(decodeURL)

