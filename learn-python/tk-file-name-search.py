"""
tk-file-name-search.py

A file name search program example to demonstrate how
to create a mouse-friendly GUI application using the 
Tkinter module.

Author:  David Briddock
Version: 1.0.3
_____________________________________________________________________


What is a GUI?
~~~~~~~~~~~~~~

A Graphical User Interface (GUI) is the software that delivers
your Raspberry Pi's desktop environment. On the official
Raspberry Pi image it's a lightweight GUI called LXDE.


Windows in Windows
~~~~~~~~~~~~~~~~~~

While each GUI application tends to look and behave differently,
they are all assembled from a collection of windows. 

Most of us recognise the typical application window frame. 
This frame has a top bar with the application's name and an
a few management buttons to iconise, maximise and close
the window.

Inside this frame there's a top-level window containing an
assortment of GUI elements, generally referred to as 'widgets'.
Buttons, labels, text boxes, images, scrollbars, sliders and
selection boxes are all types of widget. 
What you might not realise is that all these widgets are
themselves little windows. And each widget can be constructed
from many other still smaller windows. 

So, a GUI application contains a hierarchy of windows. 

Every widget has its own specific list of properties, such as
location, size and colour. 
Very importantly, a widget is alert to certain kinds of events
within its window area, such as a key press or a mouse click.
I'll cover events shortly.

If all this sounds a little complex, don't worry.
The good news is we can use a Python module called Tkinter,
which handles most of this functionality for us. 
Nevertheless, for a programmer it's important to understand
what's actually going on behind the code.


Event Handling
~~~~~~~~~~~~~~

Event handling is a critical aspect of GUI programming.
Events can be generated from many sources, the keyboard and
mouse being two obvious examples.

A GUI program must be able to determine which key was pressed.
Not just the alphanumeric keys, but also shift keys, control
keys, alt keys, function keys, cursor keys, the escape key and
special keys like the Windows key. 

As for the mouse, a program needs to determine the current
coordinates of the mouse pointer, whether a mouse button has
been clicked and if the scroll wheel has moved. 

How do we do this? 
In a GUI program it's done with something called 'callbacks'.
A callback is registered against a particular widget, and
associated with a specific function. 

When an event occurs in the widget's window area, the callback
function is called. 
This function can then determine the event type and respond
appropriately.

Once again this capability is contained within the Tkinter
module, so creating GUI callbacks is pretty straightforward.


GUI Program Structure
~~~~~~~~~~~~~~~~~~~~~

A GUI program tends to required more code than a simple
terminal-based one.
This extra code might look a little daunting to the novice
programmer, but it's not as confusing as it might seem.

Every GUI application has a very similar structure. 
Once we understand this structure we'll be able to create
many different GUI programs.

A typical GUI program has five elements:

- create the top-level window 
- create some widgets
- initialise the window and widgets
- start the main window display loop
- handle user events

This program demonstrates each of these elements.

"""
 
from Tkinter import * 
import os

# initialise top-level window and widgets
def winInit(win):
  
   #set the window title
   win.title("File Name Search App (v1.03)")
   
   # ensure we can see these variable from any function
   global pathEntry, textEntry, fileList, searchBtn
  
   # create a file path label and entry field widgets
   pathLabel = Label(win, text="Search Path")
   pathEntry = Entry(win, width=15)
   # create a search text label and entry field widgets
   textLabel = Label(win, text="Search Text")
   textEntry = Entry(win, width=15)
   # create a listbox widget to contain the matched files
   fileList = Listbox(win, width=80)
   # create a vertical scrollbar widget
   yscroll = Scrollbar(win, orient=VERTICAL)
   # create a search button widget with a callback to 'doSearch'
   searchBtn = Button(win, text="Search", width=10, command=doSearch)

   # layout the label and entry fields in a grid pattern
   # and align them using the 'sticky' option
   pathLabel.grid(row=0, column=0, sticky="W")
   pathEntry.grid(row=1, column=0)
   textLabel.grid(row=2, column=0, sticky="W")
   textEntry.grid(row=3, column=0)
   # position the button below the labels and entry fields
   searchBtn.grid(row=4, column=0)
   # position the listbox and make it 5 rows high
   fileList.grid(row=0, column=1, rowspan=5)
   # position the scroll bar next to the listbox
   # and ensure it will be stretched to the full 5 rows
   yscroll.grid(row=0, column=2, rowspan=5, sticky="NS")
         
   # attach the scrollbar to the listbox
   fileList.configure(yscrollcommand = yscroll.set)
   yscroll.configure(command = fileList.yview)
   
   # put default values in the entry fields
   pathEntry.insert(INSERT, "/home")
   textEntry.insert(INSERT, ".py")


# find button callback
def doSearch():
   # get start directory and file ending
   searchPath = pathEntry.get()
   searchString = textEntry.get() 
   
   # clear the listbox
   fileList.delete(0, END)
   
   # find every file in the path and its subdirectories
   for path, dirs, files in os.walk(searchPath):
      # process each file
      for fileName in files:
         # test for a string match in the file name 
         if (searchString in fileName):
            # found a match 
            # so add the file name to the listbox
            fileList.insert(END, path+"/"+fileName)


# create top-level window object
win = Tk()

# initialise window and widgets
winInit(win)

# run the main loop to display the window
mainloop()
