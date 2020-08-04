from pytube import YouTube

def audioDownload(url, outputPath, outputFilename):
    yt = YouTube(url)
    yt.streams.filter(only_audio=True,file_extension='mp4').first().download(output_path=outputPath, filename=outputFilename)

if __name__ == "__main__":
    audioDownload('https://www.youtube.com/watch?v=_aZWuro1fVI', '../mp4', "output.mp4")
