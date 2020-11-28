from tkinter import *
from cc_scraper import start

def get():
    uname = k.get()
    fname = l.get()
    start(uname, fname)
    
window=Tk()
window.title('CodeChef Solution Scrapper')
window.geometry('700x400')

k = StringVar()
l = StringVar()

user_label = Label(master=window, text="Username :")
user_label.pack()
user_label.place( y=40 )

dwnld_label = Label(master=window, text="Download Folder Location :")
dwnld_label.pack()
dwnld_label.place( y=140 )
 
user = Entry(master=window, width=45, textvariable=k)
user.place(x=100, y=40)

folder = Entry(master=window, width=45, textvariable=l)
folder.place(x=200, y=140)

plot_button = Button(master=window, command=get, height=2, width=15, text="Download Solutions")
plot_button.pack()
plot_button.place(relx=0.5, rely=0.6, anchor=CENTER)
