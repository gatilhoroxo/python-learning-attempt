#ele identifica como bot
import yt_dlp as yt

url = "https://www.youtube.com/watch?v=xrZX47RbeJs"

ydl_opts = {}

with yt.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video downloaded successfully!")