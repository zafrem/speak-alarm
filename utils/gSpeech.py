from google_speech import Speech
import os, datetime, sys

def textToSpeech(text):

    try :
        sox_effects=("speech", "1.5")
        sox_effects=("vol", "0.1")

        lang="en_US"
        now_time = datetime.datetime.now().strftime("%Y %H %M %d%m")
        speech = Speech(now_time, lang)
        speech.play(sox_effects)

        lang="ko_KR"
        speech = Speech(text, lang)
        speech.play(sox_effects)
    except Exception as ex:
        print("Exception sox Error(google speech).")

    print("[" + now_time + "] Text : " + text)

def _textToSpeech(text):
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H%M")
    print("[" + now_time + "] Text to Speech : " + text)

if __name__ == "__main__":
    textToSpeech("Hi Google Speech")
