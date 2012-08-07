# A timer countdown program
# Created by David - July 2012

import time

# get the countdown time in seconds
seconds = input("Number of seconds: ")

startTime = time.time()
finishTime = startTime + seconds

# loop until the current system time 
# is greater than the finishTime
while time.time() < finishTime:

   # show loop is running
   print "."
   
   # wait for one second
   time.sleep(1)

print "Time is up!"