#!/bin/bash
pip install -r requirements.txt --break-system-packages
return = $?
if [ $? -eq 0 ]; then 
  printf("Setup is done, you can run the script now using python3 main.py")
else 
  printf("Setup failed with return code $return")
