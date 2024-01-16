# Clear the screen

import os

for i in range(10):
  print(i)
  os.system("clear") # Clears numbers immediately after they appear on screen

# Clear screen after a pause

import time, os

for i in range(10):
  print(i)
  time.sleep(1) # Pauses the script for 1 second
  os.system("clear") # Clears numbers immediately after they appear on screen

