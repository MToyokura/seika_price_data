import os
import codecs


read_files_folder = 'extracted_files'
write_files_folder = 'extracted_files_UTF8converted'
os.mkdir(write_files_folder)
file_list = os.listdir(read_files_folder)
for i in file_list:
    read_file_path = os.path.join(read_files_folder, i)
    write_file_path = os.path.join(write_files_folder, i)
    with codecs.open(read_file_path, 'r', 'cp932') as rf:
        u = rf.read()
    with codecs.open(write_file_path, 'w', 'utf-8') as wf:
        wf.write(u)
