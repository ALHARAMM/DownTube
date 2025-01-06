import yt_dlp

print(r'''
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
        'format': 'bestvideo+bestaudio/best',  # Download the best video and audio
        'merge_output_format': 'mp4',  # Ensure the final output is in MP4 format
        'outtmpl': '%(title)s.%(ext)s',  # Save video with its title
        'noplaylist': True,  # Avoid downloading playlists (just the single video)
        'progress_hooks': [my_hook],  # Show download progress
        'postprocessors': [
            {  # Convert the video to MP4 if necessary
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }
        ]
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
