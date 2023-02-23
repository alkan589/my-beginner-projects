import requests
from tkinter import *
from bs4 import BeautifulSoup
#Create main window
root=Tk()

#Create Title
title = Label(root, text = "Wikipedia App").pack()

# Create Entry
str_=StringVar(root)
entry=Entry(root,textvariable = str_,width=30,fg="blue",bd=3,selectbackground='violet').pack()

#Create button
btn=Button(root,background="red",text="Summarize",height=3,width=30,command=lambda: get_data()).pack()


#Text Widget 
#Input text
inputtxt = Text(root, height = 100,
                width = 55,
                bg = "light yellow")

#Http operations
URL=f"https://tr.wikipedia.org/wiki/{str_.get()}"
response=requests.get(URL)
soup=BeautifulSoup(response.content,"lxml")
##????? If you want to complete you could tell me.
content=soup.contents
#Function
def get_data():
    inputtxt.insert(INSERT,content)
    inputtxt.insert(END,".")
    inputtxt.pack()
    
 
root.mainloop()