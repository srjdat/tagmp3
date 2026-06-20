### README is AI generated so there may be errors. 
# Spotify Local File Tagger

## What it does

Getting customized local files to show up correctly on Spotify (with the right artist, album, and cover art) is pretty tedious and annoying on every system. This project simplifies that by downloading a track from YouTube and automatically tagging it with the metadata Spotify needs, so it shows up properly in your local files.

## Requirements

- Python 3
- `eyeD3` (`pip install eyeD3`)
- A YouTube downloader (e.g. `yt-dlp`)

## Setup

1. Create a folder named `spotify local music` on your Desktop. Update the path in the program (change `user` to your local username and keep `{input_tokens[0]}.mp3` at the end) to point to this folder.
2. Make sure Spotify is set to show local files from this folder:
   - Go to **Settings → Local Files**
   - Toggle **Show Local Files** on
   - Add your `spotify local music` folder as a source

## Making it global (Linux)

To run the script as a command from anywhere on your system:

```bash
chmod +x tagmp3.py
mv tagmp3.py ~/.local/bin/tagmp3
```

Make sure `~/.local/bin` is in your `PATH`. You can check with:

```bash
echo $PATH
```

If it's not there, add this to your `~/.bashrc` (or `~/.zshrc`):

```bash
export PATH="$HOME/.local/bin:$PATH"
```

## Usage

```bash
tagmp3
> "Artist" "Album" "Album Artist" "path/to/cover.jpg" "YouTube link"
```

**Arguments (in order):**

1. **Artist**
2. **Album**
3. **Album Artist**
4. **Front cover** — path to a `.jpg` image file
5. **YouTube link** — the song to download

The program downloads the audio from the YouTube link, then applies the tags and cover art automatically.

> **Note:** Wrap each argument in quotes. Use spaces only — no commas, periods, or other punctuation needed to separate values, since each one is its own argument.

## After running

Spotify caches local file metadata, so it won't always pick up changes automatically. To force a rescan:

1. Go to **Settings → Local Files**
2. Toggle **Show Local Files** off, then back on (or remove and re-add the folder)
3. Your newly tagged track should now appear with the correct metadata and cover art

## Known limitations

- Spotify on Linux doesn't always display embedded cover art reliably, even when it's correctly tagged in the file. This is a Spotify client limitation, not a tagging issue.
- New files sometimes require a manual local files toggle/rescan to appear, even after running the script.
