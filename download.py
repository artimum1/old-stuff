import sys
from pytube import YouTube

# Get video URL from command line argument
if len(sys.argv) < 2:
    print("Please provide a YouTube video URL as an argument.")
    sys.exit()
url = sys.argv[1]

# Create YouTube object from URL
yt = YouTube(url)

# Print available video streams
print("Available video streams:")
for stream in yt.streams.filter(file_extension='mp4').order_by('resolution'):
    print(stream.resolution)

# Prompt user for desired video stream
while True:
    resolution = input("Enter desired video quality (e.g. 720p, 480p): ")
    stream = yt.streams.filter(res=resolution, file_extension='mp4', progressive=True).first()
    if stream:
        break
    print("Invalid quality. Please try again.")

# Download video
print("Downloading video...")
stream.download()
print("Video downloaded.")
