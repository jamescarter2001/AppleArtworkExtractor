# AppleArtworkExtractor

Command line tool for extracting high resolution album art from Apple Music.

## Setup

```bash
pip install -r requirements.txt
```

## Usage

Navigate to an album on Apple Music that you wish to extract album art for and copy the URL. Then use it in the following command:

```bash
python main.py -i https://music.apple.com/example -r REGION_CODE
```