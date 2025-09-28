#!/usr/bin/env python3
"""
YouTube Video Downloader
Download individual YouTube videos as MP4 files using yt-dlp.
"""

import yt_dlp 
import os
import sys
from pathlib import Path

def download_youtube_video(url, output_folder="downloads", quality="best"):
    """
    Download a single YouTube video as MP4.
    
    Args:
        url (str): YouTube video URL
        output_folder (str): Folder to save the video
        quality (str): Video quality - "best", "worst", "720", "480", etc.
    
    Returns:
        bool: True if download successful, False otherwise
    """
    
    # Create output folder if it doesn't exist
    Path(output_folder).mkdir(exist_ok=True)
    
    # Configure download options
    options = {
        'format': f'{quality}[ext=mp4]/best[ext=mp4]/best',
        'outtmpl': os.path.join(output_folder, '%(title)s.%(ext)s'),
        'writeinfojson': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(options) as downloader:
            print("Getting video information...")
            
            # Get video info first
            video_info = downloader.extract_info(url, download=False)
            title = video_info.get('title', 'Unknown Video')
            duration = video_info.get('duration', 0)
            uploader = video_info.get('uploader', 'Unknown')
            
            # Display video info
            print(f"Title: {title}")
            print(f"Channel: {uploader}")
            print(f"Duration: {duration // 60}:{duration % 60:02d}")
            print(f"Save location: {output_folder}/")
            
            # Ask for confirmation
            confirm = input("Download this video? (y/n): ").lower().strip()
            if confirm not in ['y', 'yes']:
                print("Download cancelled.")
                return False
            
            # Download the video
            print("Starting download...")
            downloader.download([url])
            
            print("Download completed successfully!")
            return True
            
    except Exception as error:
        print(f"Error: {error}")
        return False

def main():
    """Main function to run the downloader."""
    
    print("YouTube Video Downloader")
    print("-" * 25)
    
    while True:
        # Get YouTube URL
        video_url = input("Enter YouTube video URL (or 'quit' to exit): ").strip()
        
        if video_url.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
            
        if not video_url:
            print("Please enter a valid URL.")
            continue
            
        # Check if it's a valid YouTube URL
        if 'youtube.com' not in video_url and 'youtu.be' not in video_url:
            print("Please enter a valid YouTube URL.")
            continue
        
        # Get optional settings
        print("Optional settings (press Enter for defaults):")
        
        folder = input("Download folder [downloads]: ").strip()
        if not folder:
            folder = "downloads"
        
        quality = input("Quality (best/720/480/worst) [best]: ").strip()
        if not quality:
            quality = "best"
        
        # Download the video
        success = download_youtube_video(video_url, folder, quality)
        
        if success:
            print(f"Video saved in '{folder}' folder")
        
        # Ask if user wants to download another video
        another = input("Download another video? (y/n): ").lower().strip()
        if another not in ['y', 'yes']:
            print("Thanks for using the downloader!")
            break

if __name__ == "__main__":
    # Check if yt-dlp is installed
    try:
        import yt_dlp
    except ImportError:
        print("Required library not found!")
        print("Please install yt-dlp first:")
        print("pip install yt-dlp")
        sys.exit(1)
    
    main()