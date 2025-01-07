import yt_dlp
import os

print(r'''
   ____                       ______     _       
  (|   \                     (_) |      | |      
   |    | __           _  _      |      | |   _  
  _|    |/  \_|  |  |_/ |/ |   _ ||   | |/ \_|/  
 (/\___/ \__/  \/ \/    |  |_/(_/  \_/|_/\_/ |__/

@Copyright: ALHARAMM
''')

def sanitize_filename(filename):
    """Sanitize filenames to avoid issues with special characters."""
    return "".join(c if c.isalnum() or c in " _-()" else "_" for c in filename)

def download_video(url):
    # Set up options for yt-dlp to download video in 232 format and best audio
    ydl_opts = {
        'format': '232+bestaudio',  # Download format ID 232 and best audio
        'merge_output_format': 'mp4',  # Ensure the final output is in MP4 format
        'outtmpl': '%(title)s.%(ext)s',  # Save video with its title
        'noplaylist': True,  # Avoid downloading playlists
        'postprocessors': [
            {  # Merge video and audio using FFmpeg
                'key': 'FFmpegMerger'
            }
        ]
    }

    try:
        # Create a downloader instance
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Fetch video information
            info_dict = ydl.extract_info(url, download=False)
            video_title = sanitize_filename(info_dict.get("title", "video"))
            
            print(f"\nDownloading video: {video_title}")
            ydl.download([url])
            print(f"Download complete: {video_title}.mp4")

    except yt_dlp.utils.DownloadError as e:
        print(f"Download Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

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
