# himePicParser

[English](./README.md)｜繁體中文  
一款下載 mltd.matsurihi.me 中指定頁面所有圖片的工具

## Usage

```console
$ python3 himePicParser.py -B -U
usage: himePicParser [-h] [-U URL [URL ...]] [-D DIR]

Fetch all url in the matsurihi.me html elements

options:
  -h, --help            show this help message and exit
  -U URL [URL ...], --url URL [URL ...]
  -D DIR, --dir DIR
```

## Build

### [Requirements](./requirements.txt)

```console
pip install -r requirements.txt
```

```plain text
aiohttp==3.8.4
aiosignal==1.3.1
altgraph==0.17.3
async-timeout==4.0.2
attrs==23.1.0
beautifulsoup4==4.12.2
certifi==2023.5.7
charset-normalizer==3.1.0
frozenlist==1.3.3
idna==3.4
multidict==6.0.4
pyinstaller==5.13.0
pyinstaller-hooks-contrib==2023.5
requests==2.31.0
soupsieve==2.4.1
urllib3==2.0.3
yarl==1.9.2
```

#### 選項說明

- `-U` 是網頁 URL，必須以 `https://mltd.matsurihi.me` 開頭，提供複數 URL 處理
- `-D` 決定圖片被儲存的資料夾，其結構為 `./<dir>/CARD_ID`，預設為 `./`

#### 參數參考

- `-B` 抑制 `__pycache__` 的建立
- 使用空格分割各個 URL

```console
python3 -B himePicParser.py https://mltd.matsurihi.me/cards/1945 https://mltd.matsurihi.me/cards/1926
```
