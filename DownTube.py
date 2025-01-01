import yt_dlp
print (r'''
   ____                       ______     _       
  (|   \                     (_) |      | |      
   |    | __           _  _      |      | |   _  
  _|    |/  \_|  |  |_/ |/ |   _ ||   | |/ \_|/  
 (/\___/ \__/  \/ \/    |  |_/(_/  \_/|_/\_/ |__/
@Copyright: ALHARAMM
''')

def download_video(url):
    # Set up options for yt-dlp
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio, or the best if merged is unavailable
        'outtmpl': '%(title)s.%(ext)s',  # Save video with its title
        'noplaylist': True,  # Avoid downloading playlists (just the single video)
        'progress_hooks': [my_hook]  # Optional: Show download progress
    }

    # Create a downloader instance
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Optional: Hook to show download progress
def my_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['filename']} - {d['_percent_str']} at {d['_speed_str']}")
    elif d['status'] == 'finished':
        print(f"Finished downloading: {d['filename']}")

if __name__ == "__main__":
    # Provide the URL of the YouTube video you want to download
    video_url = input("Enter YouTube video URL: ")
    download_video(video_url)
