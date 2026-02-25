# Program 1 – YouTube Mashup Creator (Command Line Version)

## Objective

This program creates an audio mashup from YouTube videos of a specified singer using Python and PyPI libraries. It downloads videos, extracts audio, trims a fixed duration, and merges all clips into a single mashup file.

---

## Libraries Used (PyPI)

* yt-dlp – Download YouTube videos
* moviepy – Extract audio from video
* pydub – Trim and merge audio
* tqdm – Progress tracking

External dependency:

* FFmpeg – Required for audio processing

---

## Folder Structure

```
Program 1
│
├── 102497014.py
├── mashup.mp3
├── audio/
├── trimmed/
├── videos/
└── README.md
```

---

## Installation

Install required libraries:

```
pip install yt-dlp moviepy pydub tqdm
```

Verify FFmpeg installation:

```
ffmpeg -version
```

---

## How to Run

Command format:

```
python 102497014.py "<Singer Name>" <Number of Videos> <Duration in seconds> <Output File>
```

Example:

```
python 102497014.py "Arijit Singh" 10 30 mashup.mp3
```

---

## Workflow

The program performs the following steps:

1. Searches YouTube videos of the given singer
2. Downloads videos
3. Extracts audio
4. Trims specified duration
5. Merges all audio clips
6. Creates final mashup file

---

## Output

Generated file:

```
mashup.mp3
```

---

