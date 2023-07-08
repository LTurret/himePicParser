# himePicParser

[English](./README.md)｜繁體中文  
一款下載 mltd.matsurihi.me 中指定頁面所有圖片的工具

## 使用方法

```console
$ python3 himePicParser.py -B -U
usage: himePicParser [-h] [-U URL [URL ...]] [-D DIR]

Fetch all url in the matsurihi.me html elements

options:
  -h, --help            show this help message and exit
  -U URL [URL ...], --url URL [URL ...]
  -D DIR, --dir DIR
```

### 選項說明

- `-U` 是網頁 URL，必須以 `https://mltd.matsurihi.me` 開頭，提供複數 URL 處理
- `-D` 決定圖片被儲存的資料夾，其結構為 `./<dir>/CARD_ID`，預設為 `./`

## 建置

### 安裝依賴項

```console
pip install -r requirements.txt
```

### 執行

```console
python3 -B himePicParser.py https://mltd.matsurihi.me/cards/1945 https://mltd.matsurihi.me/cards/1926
```

- `-B` 抑制 `__pycache__` 的建立
- 使用空格分割各個 URL

### 發布

```console
pyinstaller -F himePicParser.py -i "icon.ico"
```

## 授權

遵守 [MIT](./LICENSELICE) 授權條款。
