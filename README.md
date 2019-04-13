# seika_price_data
青果物卸売市場調査（日別調査）の2010年から2018年のデータを取得し、各都市別に分けためのコードです。

## データ取得の順番
以下の順番で実行するとデータが取得できると思います。

1. monthly_scraper.py <- 各月のCSVをZIP形式で取得し保存する
2. zip_extracter.py <- 取得したZIPを解凍する
3. utf8_converter.py <- エンコードを元ファイルの "Shift JIS" から、"UTF-8" に変更する
4. file_sorter.py <- 各都市別に振り分ける