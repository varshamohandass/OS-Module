import os
import time

def mod_date(path, mod_dict):
    # Specify the file path
    file_path = r'C:\Soft Mania\Usecase 3\mkdir\folder_40\file_1.json'

    # Get the creation and modification timestamps
    creation_timestamp = os.path.getctime(file_path)
    modification_timestamp = os.path.getmtime(file_path)

    print(creation_timestamp)
    print(modification_timestamp)

    

if __name__ == "__main__":
  base_dir = r'C:\Soft Mania\Usecase 3\mkdir'
  mod_date = {}
  mod_date['path'] = ''
  mod_date['creation_time'] =''
  mod_date['modification_time'] =''
  print(mod_date)
  for root, dirs, files in os.walk(base_dir):
    for dir in dirs:
       path = os.path.join(base_dir,dir)
       mod_date(path)