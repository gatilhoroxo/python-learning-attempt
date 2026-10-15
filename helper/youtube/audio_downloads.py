#ele identifica como bot
from pytubefix import YouTube as y

url = "https://www.youtube.com/watch?v=xrZX47RbeJs"
yt = y(url)

audio_stream = yt.streams.filter(only_audio=True).first()
audio_stream.download()

