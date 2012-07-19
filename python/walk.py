# A file search program 
# Created by David - July 2012

import os

root = raw_input("Start directory? ")
ending = raw_input("File ending? ")

# walk through all the files and 
# sub-directories starting from the
# specified root directly
for path, dirs, files in os.walk(root):
   
   # step through each file in the collection
   for fileName in files:
      
      # does the file name ending match?
      if fileName.endswith(ending):
         print path + "/" + fileName