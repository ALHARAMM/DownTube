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
    # Set up options for yt-dlp to always download mp4
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/mp4',  # Download only mp4 video and audio
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
        try:
            # List available formats
            info_dict = ydl.extract_info(url, download=False)
            formats = info_dict.get('formats', [])
            print("Available formats:")
            for f in formats:
                # Print only MP4 formats
                if f.get('ext') == 'mp4':
                    resolution = f.get('height', 'N/A')
                    format_id = f['format_id']
                    print(f"Resolution: {resolution}p - Format ID: {format_id}")

            # Prompt user to choose the format
            selected_format = input("Enter the format ID you want to download: ").strip()

            # Update the format option and download
            ydl_opts['format'] = selected_format
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])

        except yt_dlp.utils.DownloadError as e:
            print(f"Error: {e}")

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
