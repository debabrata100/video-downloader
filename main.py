import yt_dlp
import os


def download_short(url: str, output_path: str = "./downloads") -> bool:
    try:
        os.makedirs(output_path, exist_ok=True)

        options = {
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "format": "best[ext=mp4]/best",  # 👈 single format, no merging needed
            "quiet": False,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        return True

    except Exception as e:
        print(f"Download failed: {e}")
        return False


def main():
    video_id = input("Enter YouTube Shorts Video ID: ").strip()
    url = f"https://www.youtube.com/shorts/{video_id}"
    download_short(url, "./downloads")


if __name__ == "__main__":
    main()
