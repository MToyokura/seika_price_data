import os
import shutil

def tk_ty_identifier(file_name):
    if i.find('tk') != -1:
        return 'k'
    elif i.find('ty') != -1:
        return 'y'

read_folder = 'extracted_files_UTF8converted'
parent_write_folder = 'extracted_files_UTF8converted_sorted'
os.mkdir(parent_write_folder)
regions = ['hirosima', 'hukuoka', 'kanazawa', 'kitakyu', 'kobe', 'kyoto', 'nagoya', 'okinawa',
           'oosaka', 'sapporo', 'sendai', 'takamatu', 'tokyo', 'total', 'yokohama']
for region in regions:
    os.mkdir(os.path.join(parent_write_folder, region))
    os.mkdir(os.path.join(parent_write_folder, region, 'k'))
    os.mkdir(os.path.join(parent_write_folder, region, 'y'))

total = regions.pop(regions.index('total'))

read_files_list = os.listdir(read_folder)

for i in read_files_list:
    copy_src = os.path.join(read_folder, i)
    if i.find('kk.csv') != -1:
        # print(os.path.join(parent_write_folder, 'total','k' ,i))
        copy_dst = os.path.join(parent_write_folder, 'total','k' ,i)
    elif i.find('ky.csv') != -1:
        # print(os.path.join(parent_write_folder, 'total','y' ,i))
        copy_dst = os.path.join(parent_write_folder, 'total','y' ,i)
    else:
        for u in regions:
            if i.find(u) != -1:
                y_or_k = tk_ty_identifier(i)
                copy_src = os.path.join(read_folder, i)
                copy_dst = os.path.join(parent_write_folder, u, y_or_k ,i)
    print(copy_src,'\n',copy_dst)
    shutil.copyfile(copy_src, copy_dst)
    
