# total の k と y をそれぞれsqlite3のデータベースに入れる

import os
import pandas as pd
import numpy as np
import sqlite3

database = 'seika_ver3.0.db'  # 'seika_ver2.1.db'

for k_or_y in ['k', 'y']:
    # まず/extracted_files_UTF8converted_sorted/total/k(またはy) にあるファイルをリストアップする。
    csv_files_list = os.listdir(os.path.join('extracted_files_UTF8converted_sorted', 'total', k_or_y))
    # dataframesという空のリストに次々とデータフレームを入れ、最後にconcat()する。
    # 一つ一つのデータフレームでconcat()していると最後のほうが遅くなってしまう。
    # https://pandas.pydata.org/pandas-docs/stable/user_guide/merging.html 
    # "It is worth noting that concat() (and therefore append()) makes a full copy of the data, and that constantly reusing this function can create a significant performance hit. If you need to use the operation over several datasets, use a list comprehension."
    # ここではlist comprehensionではなく、単純にリストにデータフレームを入れて最後にpd.concat()する。
    dataframes = []
    for i in csv_files_list:
        csv_path = os.path.join('extracted_files_UTF8converted_sorted', 'total', k_or_y, i)
        print(csv_path)
        temp_df = pd.read_csv(csv_path)
        dataframes.append(temp_df)        
    df = pd.concat(dataframes, ignore_index=True)

    # >>> df.iloc[14]
    # 年            2010
    # 月               1
    # 日               6
    # 曜日              水
    # 品目名          ネーブル
    # 品目コード       41201
    # 産地名           NaN
    # 産地コード         NaN
    # 数量           2206
    # 価格            145
    # 対前日比（数量）        －
    # 対前日比（価格）        －

    # >>> df.iloc[20]
    # 年             2010
    # 月                1
    # 日                6
    # 曜日               水
    # 品目名           いよかん
    # 品目コード        41301
    # 産地名            NaN
    # 産地コード          NaN
    # 数量          191781
    # 価格             213
    # 対前日比（数量）    ******
    # 対前日比（価格）     202.9

    # >>> df.iloc[10405]
    # 年            2010
    # 月               8
    # 日               6
    # 曜日              金
    # 品目名            くり
    # 品目コード       45700
    # 産地名           NaN
    # 産地コード         NaN
    # 数量              0
    # 価格              …
    # 対前日比（数量）        …
    # 対前日比（価格）        …

    # 上の'…'、'－'、'******'をNaNにして価格、対前日比（数量）、対前日比（価格）のdtypesを数値に揃えたい。
    # まずそれぞれをnumpyのNaNに変える。
    df = df.replace('…', np.NaN)
    df = df.replace('－', np.NaN)
    df = df.replace('******', np.NaN)
    # 価格の列をpd.to_numeric()する。
    # pd.to_numeric()するとfloat64になってしまう。整数値にしたいがNaNはfloatであるためintにはできないらしい。
    df['価格'] = pd.to_numeric(df['価格'])
    df['対前日比（数量）'] = pd.to_numeric(df['対前日比（数量）'])
    df['対前日比（価格）'] = pd.to_numeric(df['対前日比（価格）'])

    # 以下できあがったdfをsqlite3のデータベースにsqlとして保存する。
    print('total_'+k_or_y, 'を', database, 'に記録します。')

    conn = sqlite3.connect(database)
    # 下の行で、seika.db に total_ k_or_y というテーブルを記入している
    df.to_sql('total_'+k_or_y, conn) # if_exists='append')

    print('total_'+k_or_y, 'の', database, 'への記録が終了しました。')


# sqlite3での読み込み方
# import sqlite3
# conn = sqlite3.connect('seika_ver2.db')
# c = conn.cursor()
# a = c.execute('SELECT * FROM total_y LIMIT 10')
# for i in a:
#    print(i)