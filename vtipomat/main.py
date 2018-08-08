import tkinter as tk
import time
import pymysql
from database import ConnectToDB
#setup database
global database
connect = ConnectToDB()
database = connect.cursor(pymysql.cursors.DictCursor)
def GetRandomJoke():
    database.execute("SELECT * FROM jokes ORDER BY RAND() limit 1")
    return database.fetchone()

def SetShowTime(jokeLength):
    showTime = jokeLength * 75
    return showTime

def Draw():
    global text
    text=tk.Label(
        text='Welcome',
        pady = 100)
    text.pack()

def Refresher():
    global text
    jokeInfo = GetRandomJoke() 
    showTime = SetShowTime(jokeInfo['joke_length'])
    text.configure(text=jokeInfo['joke'])
    text.config(wrap=1000, font=("Helvetica", 25) )
    root.after(showTime, Refresher)


root=tk.Tk()
root.attributes('-fullscreen', True)
Draw()
Refresher()
root.mainloop()