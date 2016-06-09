import tkinter as tk
import subprocess
from Tkinter import *
import os



class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()



    def createWidgets(self):

        self.w = Label(self, text="eRadioJockey\n", font=("Helvetica", 16))
        self.w.pack(side="top")

       
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "Compile & Play News"
        self.hi_there["command"] = self.say_hi
        self.hi_there.pack(side="top")

        self.hi_there.pack(side="top")
        self.reader = tk.Button(self, text="Newspaper Reader (Firefox)", fg="red",
                              command=self.enewspaper)
        self.reader.pack(side="top")

        self.QUIT = tk.Button(self, text="Halt", fg="blue",
                              command=self.stop)
        self.QUIT.pack(side="top")

        self.footer = Label(self, text="\nCC 2016,  Sushant Gautam", font=("Helvetica", 8))
        self.footer.pack(side="top")

    def say_hi(self):
        global process
        os.system('taskkill /f /im twisterBackEng.exe')
        os.system('taskkill /f /im vlc.exe')
        process = subprocess.Popen("eRadioJockey.py", shell=True)

    def enewspaper(self):
        global process
        os.system('taskkill /f /im twisterBackEng.exe')
        os.system('taskkill /f /im vlc.exe')
        process = subprocess.Popen("EPaperReader.py", shell=True)

    def stop(self):
        os.system('taskkill /f /im twisterBackEng.exe')
        os.system('taskkill /f /im vlc.exe')
        process.kill()
              
        
def on_closing():
        os.system('taskkill /f /im twisterBackEng.exe')
        os.system('taskkill /f /im vlc.exe')
        root.destroy()
        process.kill()
        
    

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
app = Application(master=root)
app.mainloop()

