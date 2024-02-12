#!/bin/bash
pip install -r requirements.txt
if [ $? -eq 0 ]; then
  echo "Setup is done, you can run the script now using python3 main.py"
else
  echo "Setup failed "
fi
