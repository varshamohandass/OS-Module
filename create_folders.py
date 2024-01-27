import os

base_dir = r'C:\Soft Mania\Usecase 3\mkdir'

for i in range(1,1001):
    folder_name = f'folder_{i}'
    folder_path = os.path.join(base_dir,folder_name)
    os.mkdir(folder_path)
    