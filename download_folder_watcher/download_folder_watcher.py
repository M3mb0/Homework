"""A script hwo can place all your files in a certain folder"""

import shutil
from pathlib import Path
import time

DOWNLOAD_DIR = Path.home() / "Downloads"
DOWNLOAD_CLEAN = Path.home() / "Download_clean"
MUSIC_DIR = DOWNLOAD_CLEAN / "Music"
PICTURE_DIR = DOWNLOAD_CLEAN / "Pictures"
VIDEO_DIR = DOWNLOAD_CLEAN / "Video"
EXE_DIR = DOWNLOAD_CLEAN / "Apps"
OTHERS_DIR = DOWNLOAD_CLEAN / "Others"

DOWNLOAD_CLEAN.mkdir(exist_ok=True, parents=True)
MUSIC_DIR.mkdir(exist_ok=True, parents=True)
PICTURE_DIR.mkdir(exist_ok=True, parents=True)
VIDEO_DIR.mkdir(exist_ok=True, parents=True)
EXE_DIR.mkdir(exist_ok=True, parents=True)
OTHERS_DIR.mkdir(exist_ok=True, parents=True)

initial_time_delta = DOWNLOAD_DIR.stat().st_mtime
while True:
    if DOWNLOAD_DIR.stat().st_mtime != initial_time_delta:
        initial_time_delta = DOWNLOAD_DIR.stat().st_mtime
        for path in DOWNLOAD_DIR.glob("**/*"):
            if path.suffix in [".tmp", ".crdownload"]:
                continue
            elif path.suffix in [".mp3", ".wma", ".aac"]:
                time.sleep(5)
                shutil.move(path, MUSIC_DIR)
            elif path.suffix in [".jpg", ".jpeg", ".png"]:
                time.sleep(5)
                shutil.move(path, PICTURE_DIR)
            elif path.suffix in [".mpg", ".mkv", ".flv", ".avi", ".gif", ".mov", ".wmv", ".mp4"]:
                time.sleep(300)
                shutil.move(path, VIDEO_DIR)
            elif path.suffix in [".exe"]:
                time.sleep(5)
                shutil.move(path, EXE_DIR)
            else:
                time.sleep(5)
                shutil.move(path, OTHERS_DIR)
