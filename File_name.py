import os

def files_dir(path):
  for root, dirs, files in os.walk(path):
    for file in files:
      print(file)
   
path = r'D:\4th sem\DATABASE MANAGEMENT SYSTEMS'
files_dir(path)