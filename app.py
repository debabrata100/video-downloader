import yt_dlp
import os
import glob
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)


def get_port() -> int:
    return int(os.environ.get("PORT", "8080"))


def download_short(url: str, output_path: str = "/tmp/downloads") -> str | None:
    try:
        os.makedirs(output_path, exist_ok=True)  # 👈 use /tmp on servers

        options = {
            "outtmpl": f"{output_path}/%(title)s.%(ext)s",
            "format": "best[ext=mp4]/best",
            "quiet": False,
        }

        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([url])

        files = glob.glob(f"{output_path}/*.mp4")
        return max(files, key=os.path.getctime) if files else None

    except Exception as e:
        print(f"Download failed: {e}")
        return None


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/download", methods=["GET"])
def download():
    video_id = request.args.get("video_id")

    if not video_id:
        return jsonify({"status": "error", "message": "video_id is required"}), 400

    url = f"https://www.youtube.com/shorts/{video_id}"
    file_path = download_short(url)

    if file_path:
        return send_file(file_path, as_attachment=True)
    else:
        return jsonify({"status": "error", "message": "Download failed"}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=get_port(), debug=False)
