import yt_dlp

def download_video(url):
    options = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': 'downloads/%(title)s.%(ext)s'
    }
    
    with yt_dlp.YoutubeDL(options) as ydl:
        ydl.download([url])

# Usage
url = input("Enter YouTube URL: ")
download_video(url)
print("Download complete!")