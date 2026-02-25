# Assignment – YouTube Mashup Creator

## Objective

This assignment implements a YouTube mashup generator using Python and PyPI libraries. It downloads videos of a specified singer, extracts audio, trims clips, and merges them into a single mashup file.

Two implementations are provided:

1. Command Line Version
2. Web Service Version

---

## Libraries Used

PyPI Libraries:

* yt-dlp
* moviepy
* pydub
* flask
* tqdm

External dependency:

* FFmpeg

---

## Folder Structure

```
Assignment - Mashup
│
├── Program 1
│   ├── 102497014.py
│   ├── mashup.mp3
│   ├── audio/
│   ├── trimmed/
│   ├── videos/
│   └── README.md
│
├── Program 2
│   ├── app.py
│   ├── mashup.mp3
│   ├── mashup.zip
│   ├── templates/
│   ├── audio/
│   ├── trimmed/
│   ├── videos/
│   └── README.md
│
└── README.md
```

---

## Program 1 – Command Line Version

Run using:

```
python 102497014.py "<Singer Name>" <Number of Videos> <Duration> <Output File>
```

Example:

```
python 102497014.py "Arijit Singh" 10 30 mashup.mp3
```

---

## Program 2 – Web Version

Run using:

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

## Output

Generated files:

* mashup.mp3
* mashup.zip

---

## Requirements

* Python 3.9+
* FFmpeg installed
* Internet connection

---


