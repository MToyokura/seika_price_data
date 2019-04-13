import os
import zipfile

zip_list = os.listdir('zip_files')
for a in zip_list:
    print(a)
    with zipfile.ZipFile(os.path.join('zip_files', a) , 'r') as zip_ref:
        zip_ref.extractall('extracted_files')
