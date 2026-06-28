# YouTube Video Downloader

A Flask-based REST API for downloading YouTube Shorts videos with a simple HTTP interface.

## How to download
http://localhost:8080/download?video_id=<videoID>

## Overview

This project provides a lightweight web service that allows you to download YouTube Shorts videos by their video ID. The application uses `yt-dlp` for video downloading and Flask for the web API, making it easy to integrate into other applications or use via simple HTTP requests.

## Features

- **REST API**: Simple HTTP endpoint for downloading videos
- **Automatic Quality Selection**: Automatically selects the best available MP4 format
- **File Management**: Saves videos to a local `downloads` folder
- **Error Handling**: Graceful error handling with meaningful HTTP responses
- **Direct Download**: Browser-compatible file streaming for downloaded videos

## Prerequisites

- **Python**: 3.14 or higher
- **FFmpeg**: Required for video conversion
  ```bash
  brew install ffmpeg
  ```

## Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd video-downloader
   ```

2. **Install dependencies using UV**
   ```bash
   uv sync
   ```
   
   Or with pip:
   ```bash
   pip install flask yt-dlp
   ```

3. **Activate the virtual environment** (if using UV)
   ```bash
   source .venv/bin/activate
   ```

## Usage

### Starting the Server

```bash
python main.py
```

The server will start on `http://localhost:8080`

### API Endpoint

**Download a YouTube Short**

```
GET /download?video_id=<video_id>
```

**Parameters:**
- `video_id` (required): The YouTube video ID from the shorts URL

**Example:**

```bash
curl "http://localhost:8080/download?video_id=dQw4w9WgXcQ" -o video.mp4
```

**Success Response:**
- Status: `200 OK`
- Body: Video file (MP4)

**Error Response:**
- Status: `400 Bad Request` - Missing `video_id` parameter
- Status: `500 Internal Server Error` - Download failed

### Example Usage

To download a Short from `https://www.youtube.com/shorts/dQw4w9WgXcQ`:

```bash
curl "http://localhost:8080/download?video_id=dQw4w9WgXcQ" -o my_video.mp4
```

## Project Structure

```
video-downloader/
├── main.py           # Flask application and download logic
├── pyproject.toml    # Project configuration and dependencies
├── README.md         # This file
└── downloads/        # Downloaded videos (created at runtime)
```

## Technical Details

- **Framework**: Flask 3.1.3+
- **Video Downloader**: yt-dlp 2026.3.17+
- **Video Format**: MP4 (best quality available)
- **Download Location**: `./downloads/` (created automatically)

## Requirements

All dependencies are listed in `pyproject.toml`:
- `flask>=3.1.3` - Web framework for the REST API
- `yt-dlp>=2026.3.17` - YouTube video downloading

## Development

To run in development mode with auto-reload:

```bash
python main.py
```

The Flask development server includes hot-reloading capabilities.

## Docker

Build the Docker image:

```bash
docker build -t video-downloader:latest .
```

Run the container (maps container port 8080 to host port 8080):

```bash
docker run --rm -p 8080:8080 --name video-downloader video-downloader:latest
```

Then call the API at `http://localhost:8080/download?video_id=<videoID>`.
