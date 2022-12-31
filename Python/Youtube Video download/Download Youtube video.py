from pytube import YouTube
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
link = input("Enter youtube video URL: ")
yt = YouTube(link)
for qualities in yt.streams.filter(progressive=True):
    quality = yt.streams.get_by_resolution(resolution="720p")
    quality.download()

print("Downloading", yt.title)
print("Video Thumbnail", yt.thumbnail_url)
print("Downloaded", link)

