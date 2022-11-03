""""A script who can move files from a folder to another on a given location.
The location is read form config.txt file"""

from pathlib import Path
from datetime import datetime
import shutil

MY_FOLDER = Path(r"C:\Users\ravva\Desktop\My_folder")
ROOT = Path(__file__).parent
CONFIG_PATH = ROOT / "config.txt"
current_date = datetime.now()
folder_name = current_date.strftime("%Y-%m-%d_%H-%M")


try:
    with CONFIG_PATH.open() as fin:
        content = fin.readline()
        content = content.strip("\n")
except OSError as err:
    archive_path = Path(r"C:\Archive")
    print(f"Error {err}")
else:
    archive_path = Path(content)

archive_path.mkdir(exist_ok=True)
print(folder_name)
FOLDER_PATH = archive_path / folder_name

try:
    shutil.copytree(MY_FOLDER, FOLDER_PATH)
except FileExistsError:
    print("Backup already complete. Try after 1 min")
else:
    print("Backup complete")
