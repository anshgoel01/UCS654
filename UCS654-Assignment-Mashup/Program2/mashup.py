# mashup.py
# functions for downloading videos, converting to audio,
# cutting audio and merging them

import os
from yt_dlp import YoutubeDL
from moviepy import VideoFileClip
from pydub import AudioSegment


#vidoes download
def download_videos(singer, n):

    os.makedirs("videos", exist_ok=True)

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': 'videos/%(title)s.%(ext)s',
        'quiet': True
    }

    #searching youtube videos
    search_query = f"ytsearch{n}:{singer} songs"

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([search_query])


#audio convert
def convert_to_audio():

    os.makedirs("audios", exist_ok=True)

    for file in os.listdir("videos"):

        video_path = os.path.join("videos", file)

        if file.endswith(".mp4"):

            clip = VideoFileClip(video_path)

            audio_name = os.path.splitext(file)[0] + ".mp3"
            audio_path = os.path.join("audios", audio_name)

            # convert video -> mp3
            clip.audio.write_audiofile(audio_path)
            clip.close()


#trim and merge
def cut_and_merge(duration, output_file):

    final_audio = AudioSegment.empty()

    for file in os.listdir("audios"):

        if file.endswith(".mp3"):

            audio_path = os.path.join("audios", file)
            audio = AudioSegment.from_mp3(audio_path)

            #cutting first y seconds
            part = audio[:duration * 1000]

            final_audio += part

    #exporting final mashup
    final_audio.export(output_file, format="mp3")
