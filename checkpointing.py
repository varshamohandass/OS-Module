import os
import time
import glob
import json

def file_mod(path, mod_dict):
    os.chdir(path)
    for file in glob.glob("*.json"):
      creation_timestamp = os.path.getctime(file)
      modification_timestamp = os.path.getmtime(file)
      if modification_timestamp > mod_dict['modification_time']:
         mod_dict['modification_time'] = modification_timestamp
         mod_dict['creation_time'] = creation_timestamp
         mod_dict['path'] = os.path.join(path,file)
         with open(file, mode='r') as f:
          data = json.load(f)
          print(data)
      else:
        continue
      with open(file, mode='w') as f:
            data = json.dumps(mod_dict)


    

if __name__ == "__main__":
  base_dir = r'C:\Soft Mania\Usecase 3\mkdir'
  mod_date = {}
  mod_date['path'] = ''
  mod_date['creation_time'] =''
  mod_date['modification_time'] =''
  for root, dirs, files in os.walk(base_dir):
    for dir in dirs:
        path = os.path.join(base_dir,dir)
        file_mod(path,mod_date)
  print(mod_date)