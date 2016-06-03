from gtts import gTTS
import shutil
import time, os, glob
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import winsound, sys
from datetime import datetime
import urllib


print("eRadioJockey Project")
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
decodeURL='http://www.ekantipur.com/eng'
driver.get(decodeURL)

def speak(voicedata, num):
    print(str((newsnum+1) - num))
    tts = gTTS(text=voicedata, lang='en')
    tts.save("e:/temp/"+str(num+1)+".mp3")
    shutil.copy('E:\SandBox\Python/assets/alert.wav', 'e:/temp/')
    newname = 'ren E:\\temp\\alert.wav'+' '+str(num)+str(num)+'.wav'
    os.system(newname)
       

#find the element that's name attribute display-news-title
textw = driver.find_elements_by_class_name("display-news-title")

import glob, os
test = 'e:/temp/*'
r = glob.glob(test)
for i in r:
   os.remove(i)


newsnum = 6
x=1
while x <= newsnum :
    speak(textw[x].text, x+1)
    x += 1

datandtime = time.strftime("%B %d %Y")+time.strftime("%I %M %p")
sp = 'Hello! its e radio jockey. its' + datandtime + 'in your system now. Presenting the latest news headlines prepared specifically for you.'
speak(sp,0)

    
print("\nServing via VLC media player (WIN64). . .")
os.system("c:/progra~2/VideoLAN/VLC/vlc.exe --started-from-file --playlist-enqueue e:/temp/")

time.sleep(2)
os.system('exit')

