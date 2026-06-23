#!/usr/bin/env python3

import yt_dlp
import eyed3
from eyed3.id3.frames import ImageFrame
import os, shutil
import sys
# Cross platform path operations
from pathlib import Path
# Cross platform temp directory
import tempfile
# Fixes arrow keys not working in input()
import readline

# downloads the audio from the link 
def download_audio(url): 
    output_dir = tempfile.gettempdir()
    yt_dlp_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{output_dir}/%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',     
            'preferredquality': '192',
        }],
    }

    with yt_dlp.YoutubeDL(yt_dlp_opts) as ydl: 
        info = ydl.extract_info(url, download=True)
        filepath = ydl.prepare_filename(info)
        base = Path(filepath).stem
        final_path = Path(output_dir) / f'{base}.mp3'

    return final_path

def prompt_input():
    print("Destination folder")
    destination_input = input("> ")
    print("Title Artist Album Album_Artist Front_Cover Youtube_Link")
    user_input = input("> ")

    input_tokens = []
    input_tokenizer = ""
    quote = False

    # loop through the string
    for i in user_input:
        # check if the letter is a quote
        if i == "\"":
            quote = not quote  # if the letter is a quote we don't want to add it to the tokenizer
            # im doing inverse of quote cause if it's false then it becomes true and vice versa
        elif quote:  # check if we are in quote mode
            input_tokenizer += i
        elif i == " ":  # if the letter is a space
            input_tokens.append(input_tokenizer)  # add current word to tokens
            input_tokenizer = ""  # clear out tokenizer
        else:  # not in quote mode, not a quote, not a space, random character
            input_tokenizer += i

    input_tokens.append(input_tokenizer)  # add current token into the tokensarray
    input_tokenizer = ""  # clear tokenizer

    return destination_input, input_tokens

def main(): 
    # Prompt for input if the user passes no arguments via shell
    if len(sys.argv) > 7:
        destination_input = sys.argv[1]
        input_tokens = sys.argv[2:]
    else:
        destination_input, input_tokens = prompt_input()

    input_tokens[5] = download_audio(input_tokens[5])

    # artist, album, album_artist, front_cover, file path
    audiofile = eyed3.load(str(input_tokens[5]))
    if audiofile.tag is None:
        audiofile.initTag()

    # put all the data into the tags
    audiofile.tag.title = input_tokens[0]
    audiofile.tag.artist = input_tokens[1]
    audiofile.tag.album = input_tokens[2]
    audiofile.tag.album_artist = input_tokens[3]

    # get image for front cover first
    with open(input_tokens[4], "rb") as image_file:
        imagedata = image_file.read()

    audiofile.tag.images.set(
        ImageFrame.FRONT_COVER,
        imagedata,
        "image/jpeg",
        u"cover"
    )
    audiofile.tag.save()

    # automatically moves it to the folder where we want it 
    # made everything be in variables to make it easier to change later
    file_format = "mp3"
    final_dest = Path(destination_input) / f'{input_tokens[0]}.{file_format}' 
    shutil.move(input_tokens[5], final_dest)

if __name__ == "__main__": 
    try:
        main()
    except KeyboardInterrupt:
        print("\nProcess interrupted by user, exiting...")
