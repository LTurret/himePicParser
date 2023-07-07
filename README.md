# himePicParser

A tool for getting all the pictures url in the specificed card page that belongs to matsurihi.me

## Build

### [Requirements](./requirements.txt)

```console
pip install -r requirements.txt
```

```plain text
aiohttp==3.8.4
aiosignal==1.3.1
async-timeout==4.0.2
attrs==23.1.0
beautifulsoup4==4.12.2
certifi==2023.5.7
charset-normalizer==3.1.0
frozenlist==1.3.3
idna==3.4
multidict==6.0.4
requests==2.31.0
soupsieve==2.4.1
urllib3==2.0.3
yarl==1.9.2
```

### Usage

```console
$ python3 main.py -B -U
usage: himePicParser [-h] [-U URL [URL ...]] [-D DIR]

Fetch all url in the matsurihi.me html elements

options:
  -h, --help            show this help message and exit
  -U URL [URL ...], --url URL [URL ...]
  -D DIR, --dir DIR
```

#### Options Description

- `-U` is page URL, must start with `mltd.matsurihi.me`, Provides multi-URL handling.
- `-D` determine the folder wheres your image are be stored, which the structure is `./<dir>` and the default is `./`

#### Argument Example

- `-B` prevent `__pycache__` being created.
- Using space splits URLs respectively

```console
python3 -B main.py https://mltd.matsurihi.me/cards/1945 https://mltd.matsurihi.me/cards/1926
```

## Todo

- [ ] parse SSR pictures
