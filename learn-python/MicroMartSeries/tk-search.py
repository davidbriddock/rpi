# A GUI search program using TK
# Created by David in July 2012
 
from Tkinter import * 
import os

# initialise main window  
def init(win):  
   win.title("File Search")
   
   labelPath.grid(row=0, column=0, sticky="W")
   entryPath.grid(row=1, column=0)
   labelEnding.grid(row=2, column=0, sticky="W")
   entryEnding.grid(row=3, column=0)
   btnSearch.grid(row=4, column=0)
   fileList.grid(row=0, column=1, rowspan=5)
   yscroll.grid(row=0, column=2, rowspan=5, sticky="NS")
         
   fileList.configure(yscrollcommand = yscroll.set)
   yscroll.configure(command = fileList.yview)
   entryPath.insert(INSERT, "/home")
   entryEnding.insert(INSERT, ".py")

# find button callback
def search():
   # get start directory and file ending
   startDir = entryPath.get()
   fileEnding = entryEnding.get() 
   
   # clear the listbox
   fileList.delete(0, END)
   
   # find matching file and fill listbox
   for path, dirs, files in os.walk(startDir):
      for fileName in files:
         if (fileName.endswith(fileEnding)):
            fileList.insert(END, path+"/"+fileName)

# create top-level window object
win = Tk()

# create widgets
labelPath = Label(win, text="Starting Path")
entryPath = Entry(win, width=12)
labelEnding = Label(win, text="File Ending")
entryEnding = Entry(win, width=12)
fileList = Listbox(win, width=80)
yscroll = Scrollbar(win, orient=VERTICAL)
btnSearch = Button(win, text="Search", width=8, command=search)

# initialise and run main loop
init(win)
mainloop()
