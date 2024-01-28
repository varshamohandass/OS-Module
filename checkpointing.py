import os
import time
import glob
import json
import hashlib

def file_mod(path, mod_dict,checkpoint_path):
    os.chdir(path)
    print("Directory changed")
    for file in glob.glob("*.json"):
      print(''' file name --> ''', file)
      file_complete_path = path+"\\"+file
      file_hash = str(hashlib.md5(file.encode()).hexdigest())+".txt"
      path_hash = str(hashlib.md5(path.encode()).hexdigest())
      checkpoint_path_final = os.path.join(checkpoint_path,path_hash,file_hash)
      if not os.path.isfile(checkpoint_path_final):
         print("Looks like a new file")
         with open(file_complete_path, mode='r') as f:
          data = json.load(f)
          # print(data)
         os.chdir(checkpoint_path)
         if not os.path.isdir(path_hash):
          os.mkdir(path_hash)
         os.chdir(os.path.join(checkpoint_path,path_hash))
         file1 = open(file_hash, 'w+')
         file1.close()
      else:
        print("This file was processed already")



    

if __name__ == "__main__":
  base_dir = r'C:\Soft Mania\Usecase 3\mkdir'
  mod_date = {}
  mod_date['path'] = ''
  mod_date['creation_time'] = 0
  mod_date['modification_time'] = 0
  checkpoint_path = r'C:\Soft Mania\Usecase 3\checkpoints'
  for root, dirs, files in os.walk(base_dir):
    for dir in dirs:
        path = os.path.join(base_dir,dir)
        # print("------")
        print(path)
        # print(base_dir,dir)  # C:\Soft Mania\Usecase 3\mkdir folder_1
        # print("======")
        file_mod(path,mod_date,checkpoint_path)
        break
    break