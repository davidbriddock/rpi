import os, platform

print "Welcome to " + platform.system()
print "You are logged in as " + os.getlogin()
print "Current directory is " + os.getcwd()
print "Running Python version " + platform.python_version()