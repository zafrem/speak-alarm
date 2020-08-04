from pydub import AudioSegment
from pydub.playback import play
import os, datetime

def mp3ToSpeech(files):
    now_time = datetime.datetime.now().strftime("%H clock %M minutes")
    print("[" + now_time + "] Play  : " + files)
    song = AudioSegment.from_file(files, "mp4")
    play(song)
    os.remove(files)

if __name__ == "__main__":
    mp3ToSpeech("..\\mp4\\test.mp4")
