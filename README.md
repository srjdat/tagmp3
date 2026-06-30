# Spotify Local File Tagger

## What it does

Getting customized local files to show up correctly on Spotify (with the right artist, album, and cover art) is pretty tedious and annoying on every system. This project simplifies that by downloading a track from YouTube and automatically tagging it with the metadata Spotify needs, so it shows up properly in your local files.

## Requirements
- Python3
- ffmpeg

## Before running the program
Make sure you have a folder somewhere you are storing your local files for Spotify.

## How to get started 
1. Clone this repository
2. Go to the directory of this project and do `pip install -r requirements.txt`
3. Run `python3 installcli.py` or `python3 installgui.py` depending on whether you want CLI or GUI version. 
4. Run `tagmp3` from anywhere on your computer

## MacOS specific installation
1. Make sure to use Homebrew python3.    
2. Create a venv folder using `python3 -m venv .venv`.     
3. Activate the virtual environment by using `source .venv/bin/activate`.    
4. Add `#!/path/to/tagmp3/venv/bin/python3` to either tagmp3gui.py or tagmp3cli.py depending on what you want.   
5. Run the installation scripts. 

## Running the program
### CLI
After running `tagmp3` it will ask for the destination folder and then the tags, or you can enter all the commands after `tagmp3`    
Whenever there is a ">" symbol, it is for the user to type.      
```
usr % tagmp3
Destination folder
> /enter/path/to/folder/
Title Artist Album Album_Artist Front_Cover Youtube_Link
> "Right Now" "NewJeans" "Supernatural" "NewJeans" "/path/to/front/cover.png" "https://youtu.be/m6pTbEz4w3o?si=zhu30LJmH0YauPbw"
```
or 
```
usr % tagmp3 "/enter/path/to/folder" "Right Now" "NewJeans" "Supernatural" "NewJeans" "/path/to/front/cover.png" "https://youtu.be/m6pTbEz4w3o?si=zhu30LJmH0YauPbw"
```
> Note: When inputting Destination Folder separately (like in the first case), do not use quotes. When inputting Destination Folder with the other arguments (like in the second case), use quotes. 

### GUI
After running `tagmp3` a GUI will pop up asking for Title, Artist, Album, Cover, Youtube Link, and Destination folder.   
Cover and Destination will give you the abilitiy to choose your own through a dialog box (click select button to access the dialog box). 

![GUI Image](images/gui-image.png)   
Enter all the fields freely with no need to worry about quotes

## After running
Go to Spotify settings and turn off and on the folder that you are using for local files. 

![Spotify local files source](images/image-1.png)    
Turn this off and on

Your newly tagged track should appear with the correct metadata!

## Uninstallation
Run `python3 uninstall.py` to remove the script. 

## Additional Information
- Spotify sometimes doesn't show the cover art reliably on Linux
   - This issue isn't a fault of the program, Linux doesn't have the best support for everything
- Sometimes it will require you to turn on and off the source folder or local files in general a couple of times before this works (this is just how Spotify is). 
