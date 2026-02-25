# Program 2 – YouTube Mashup Creator (Web Service Version)

## Objective

This program provides a web interface to generate an audio mashup from YouTube videos of a specified singer. The user enters the singer name, number of videos, and duration, and the system generates a mashup audio file automatically.

---

## Technologies Used

Backend:

* Python
* Flask (web framework)
* yt-dlp (download YouTube videos)
* moviepy (extract audio)
* pydub (trim and merge audio)

Frontend:

* HTML
* CSS

External dependency:

* FFmpeg (required for audio processing)

---

## Folder Structure

```
Program 2
│
├── app.py
├── mashup.mp3
├── mashup.zip
├── templates/
│   └── index.html
├── audio/
├── trimmed/
├── videos/
└── README.md
```

---

## Installation

Install required libraries:

```
pip install flask yt-dlp moviepy pydub tqdm
```

Ensure FFmpeg is installed:

```
ffmpeg -version
```

---

## How to Run

Open terminal inside Program 2 folder:

```
python app.py
```

Open browser and go to:

```
http://127.0.0.1:5000
```

Enter:

* Singer Name
* Number of Videos
* Duration

Click Submit to generate mashup.

---

## Output

The system generates:

```
mashup.mp3
mashup.zip
```

---

## Features

* Web-based interface
* Automatic YouTube download
* Audio trimming and merging
* Mashup file generation

---

## Sample output mashup files are included for demonstration.
