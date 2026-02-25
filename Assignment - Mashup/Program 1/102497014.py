import sys
import os
import yt_dlp
from pydub import AudioSegment
from moviepy import VideoFileClip


def download_videos(singer, num):

    folder = "videos"
    os.makedirs(folder, exist_ok=True)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{folder}/%(title)s.%(ext)s',
        'quiet': False
    }

    search = f"ytsearch{num}:{singer} songs"

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([search])


def convert_to_audio():

    os.makedirs("audio", exist_ok=True)

    for file in os.listdir("videos"):

        if file.endswith(".mp4"):

            video = VideoFileClip(f"videos/{file}")

            video.audio.write_audiofile(
                f"audio/{file.replace('.mp4','.mp3')}"
            )

            video.close()


def trim_audio(duration):

    os.makedirs("trimmed", exist_ok=True)

    for file in os.listdir("audio"):

        sound = AudioSegment.from_mp3(f"audio/{file}")

        sound = sound[:duration * 1000]

        sound.export(f"trimmed/{file}", format="mp3")


def merge_audio(output):

    combined = AudioSegment.empty()

    for file in os.listdir("trimmed"):

        sound = AudioSegment.from_mp3(f"trimmed/{file}")

        combined += sound

    combined.export(output, format="mp3")


def main():

    if len(sys.argv) != 5:

        print(
            "Usage:\n"
            "python 102497014.py "
            "<SingerName> <NumberOfVideos> <Duration> <OutputFile>"
        )

        return


    singer = sys.argv[1]
    num = int(sys.argv[2])
    duration = int(sys.argv[3])
    output = sys.argv[4]


    print("Downloading...")
    download_videos(singer, num)

    print("Converting...")
    convert_to_audio()

    print("Trimming...")
    trim_audio(duration)

    print("Merging...")
    merge_audio(output)

    print("Mashup created:", output)


if __name__ == "__main__":
    main()