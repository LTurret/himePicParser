# himePicParser

English ｜[繁體中文](./README-zh-TW.md)  
A tool for downloading all the pictures in a specified card page that belongs to mltd.matsurihi.me

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

- `-U` is page URL, must start with `https://mltd.matsurihi.me`, Provides multi-URL handling
- `-D` determine the folder wheres your image are be stored, which the structure is `./<dir>/CARD_ID` and the default is `./`

## Build

### Install Dependencies

```console
pip install -r requirements.txt
```

### Run

```console
python3 -B himePicParser.py https://mltd.matsurihi.me/cards/1945 https://mltd.matsurihi.me/cards/1926
```

- `-B` prevent `__pycache__` being created
- Using SPACE splits URLs respectively

### Distribute

```console
pyinstaller -F himePicParser.py -i "icon.ico"
```

## License

Licensed under [MIT](./LICENSE)

## Todo

- [ ] parse SSR pictures
