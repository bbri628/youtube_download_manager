import os
os.environ['XDG_CACHE_HOME'] = os.path.expanduser('~/.yt-dlp-cache')
import argparse
import yt_dlp

def download(url, folder="downloads", resolution=None):
    # create folder if it doesn't exist
    if not os.path.exists(folder):
        os.mkdir(folder)

    # set up download options
    if resolution:
        fmt = f"bestvideo[height<={resolution}]+bestaudio/best"
    else:
        fmt = "best"

    options = {
        "format": fmt,
        "outtmpl": folder + "/%(title)s.%(ext)s"
    }

    try:
        print("Downloading...")
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])
        print("Done!")
    except Exception as e:
        print("Something went wrong:")
        print(e)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--output", default="downloads")
    parser.add_argument("--resolution", default=None)
    args = parser.parse_args()

    # basic check for URL
    if "youtube.com" not in args.url and "youtu.be" not in args.url:
        print("This is not a YouTube link.")
        return

    download(args.url, args.output, args.resolution)

if __name__ == "__main__":
    main()



