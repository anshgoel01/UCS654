import sys
import os
from mashup import download_videos, convert_to_audio, cut_and_merge


def main():

    try:

        if len(sys.argv) != 5:
            print("Usage: python <file.py> <SingerName> <NumberOfVideos> <AudioDuration> <OutputFileName>")
            return

        singer = sys.argv[1]
        number = int(sys.argv[2])
        duration = int(sys.argv[3])
        output_file = sys.argv[4]

        #checking
        if number <= 10:
            print("Number of videos must be greater than 10")
            return

        if duration <= 20:
            print("Audio duration must be greater than 20 seconds")
            return

        #create output folder if not exists
        os.makedirs("output", exist_ok=True)

        output_path = os.path.join("output", output_file)

        print("Downloading videos...")
        download_videos(singer, number)

        print("Converting videos to audio...")
        convert_to_audio()

        print("Cutting and merging audio...")
        cut_and_merge(duration, output_path)

        print("Mashup created successfully:", output_path)

    except Exception as e:
        print("Error occurred:", str(e))


if __name__ == "__main__":
    main()
