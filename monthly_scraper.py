# https://www.seisen.maff.go.jp/seisen/bs04b040md001/BS04B040UC020SC001-Evt007.do
# まとめてダウンロードするやつ

import requests
import time

for year in range(2010, 2019):
    for month in range(1, 13):
        for day in range (1, 4):
            s027year = str(year)
            if month < 10:
                s027month = '0' + str(month)
            else:
                s027month = str(month)
            s027tendays = str(day)
            print(s027year, s027month, s027tendays)

            payload = {'s027.sessionId':'A73643EEB3F962A029081A74E6E98CD2','s027.year': s027year, 's027.month': s027month, 's027.tendays': s027tendays, 's027.chohyoFileType': 'CSV'}
            zipped_csv = requests.post('https://www.seisen.maff.go.jp/seisen/bs04b040md001/BS04B040UC020SC002-Evt001.do', data=payload)

            if zipped_csv.status_code == 200:
                print('Status: 200')
                with open(s027year + s027month + s027tendays + '_CSV.zip', 'wb') as f:
                    for chunk in zipped_csv.iter_content(chunk_size=1024): 
                        if chunk:
                            f.write(chunk)                            
            else: print('Status: Error')
            
            time.sleep(3)

# import pdb; pdb.set_trace()