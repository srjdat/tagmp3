import sys
import shutil
import os
from pathlib import Path

def uninstall(filepath: Path):
    if os.path.exists(filepath):
        filepath.unlink()
        print("tagmp3 uninstalled successfully!")
    else:
        print("tagmp3 wasn't installed")

if sys.platform == 'win32':
    uninstall(Path.home() / "bin" / "tagmp3")
elif sys.platform == 'linux' or sys.platform == 'darwin':
    uninstall(Path.home() / ".local" / "bin" / "tagmp3")
else:
    print("Unable to uninstall")
    print(f'Unknown platform: {sys.platform}')
