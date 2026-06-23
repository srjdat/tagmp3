import sys
import shutil
import os
from pathlib import Path

def install_unix():
    tagmp3 = "tagmp3cli.py"
    install_dir = Path.home() / ".local" / "bin"
    made_local_bin = False
    # First we ensure ~/.local/bin exists
    # macOS by default doesn't have this
    # Linux generally does, unless you don't have a DE
    if not os.path.exists(install_dir):
        os.makedirs(install_dir, exist_ok=True)
        made_local_bin = True

    filepath = install_dir / "tagmp3"

    if not os.path.exists(filepath):
        shutil.copy(tagmp3, filepath)
        os.chmod(path=filepath, mode=0o755)
        print("tagmp3 installed successfully!")
    else:
        print("tagmp3 is already installed")

    if made_local_bin:
        print(f'Please add {install_dir} to your PATH')

def install_win32():
    tagmp3 = "tagmp3cli.py"
    install_dir = Path.home() / "bin"
    made_local_bin = False
    if not os.path.exists(install_dir):
        os.makedirs(install_dir, exist_ok=True)
        made_local_bin = True

    filepath = install_dir / "tagmp3"

    if not os.path.exists(filepath):
        shutil.copy(tagmp3, filepath)
        print("tagmp3 installed successfully!")
    else:
        print("tagmp3 is already installed")

    if made_local_bin:
        print(f'Please add {install_dir} to your PATH')

if sys.platform == 'win32':
    install_win32()
elif sys.platform == 'linux' or sys.platform == 'darwin':
    install_unix()
else:
    print("Unable to install")
    print(f'Unknown platform: {sys.platform}')
