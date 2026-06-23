#!/usr/bin/env python3

from pathlib import Path
import tkinter as tkr
from tkinter import ttk
from tkinter import filedialog
import yt_dlp
import eyed3
from eyed3.id3.frames import ImageFrame
import os

root = tkr.Tk()
title_str, artist_str, cover_str, album_str, link_str, dest_str = tkr.StringVar(), tkr.StringVar(), tkr.StringVar(), tkr.StringVar(), tkr.StringVar(), tkr.StringVar()

def enter_command(): 
    # end the gui cause we're done and all the tags are stored in global variables 
    root.destroy()

def select_cover_file(): 
    filename = filedialog.askopenfile()
    front_cover.insert(0, filename.name)    

def select_destination_file(): 
    filename = filedialog.askdirectory()
    destination.insert(0, filename)

def download_audio(url, output_dir="Downloads"): 
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
        base, _ = filepath.rsplit('.', 1)
        final_path = f'{base}.mp3'

    return final_path

def gui(): 
    # gui
    root.title("tagmp3")
    root.geometry('510x340')

    frame1 = ttk.Frame(root)
    frame1.grid(row=3, column=1)
    frame1.columnconfigure(0, weight=1)

    frame2 = ttk.Frame(root)
    frame2.grid(row=5, column=1)
    frame2.columnconfigure(0, weight=1)

    # all global variables cause i will be accessing these elsewhere
    global title_str, album_str, artist_str, cover_str, link_str, dest_str
    global title, album, artist, front_cover, link, destination

    # song title
    ttk.Label(root, text="Title").grid(row=0, column=0, padx=15, pady=(6, 3))
    title = ttk.Entry(root, textvariable=title_str, width=25)
    title.grid(row=0, column=1, padx=5, pady=(6, 3))

    # song album
    ttk.Label(root, text="Album").grid(row=1, column=0, padx=15, pady=3)
    album = ttk.Entry(root, textvariable=album_str, width=25)
    album.grid(row=1, column=1, padx=5, pady=3)

    # artist
    ttk.Label(root, text="Artist").grid(row=2, column=0, padx=15, pady=3)
    artist = ttk.Entry(root, textvariable=artist_str, width=25)
    artist.grid(row=2, column=1, padx=5, pady=3)

    # front_cover
    ttk.Label(root, text="Cover").grid(row=3, column=0, padx=15, pady=3)
    front_cover = ttk.Entry(frame1, textvariable=cover_str, width=17)
    front_cover.grid(row=0, column=0, padx=4, pady=3, sticky='ew')
    ttk.Button(frame1, text="Select", command=select_cover_file, width=6).grid(row=0, column=1, padx=7)

    # youtube link
    ttk.Label(root, text="Link").grid(row=4, column=0, padx=15, pady=3)
    link = ttk.Entry(root, textvariable=link_str, width=25)
    link.grid(row=4, column=1, padx=5, pady=3)

    # where to move it to 
    ttk.Label(root, text="Destination").grid(row=5, column=0, padx=15, pady=3)
    destination = ttk.Entry(frame2, textvariable=dest_str, width=17)
    destination.grid(row=0, column=0, padx=4, pady=3, sticky='ew')
    ttk.Button(frame2, text="Select", command=select_destination_file, width=6).grid(row=0, column=1, padx=7)

    # enter button
    button = ttk.Button(root, text="Enter", command=enter_command)
    button.grid(row=6, column=0, columnspan=2, pady=15)



    root.mainloop()

def main(): 

    # make the list with all the things we get from the gui
    input_tokens = [None] * 6
    input_tokens[0] = title_str.get()
    input_tokens[1] = artist_str.get()
    input_tokens[2] = album_str.get()
    input_tokens[3] = artist_str.get()
    input_tokens[4] = cover_str.get()
    input_tokens[5] = link_str.get()

    
    input_tokens[5] = download_audio(input_tokens[5])
    print(input_tokens[5])

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
    audiofile.tag.save() # save everything

    # have to figure this out
    dest_filepath = Path(dest_str.get())
    format = ".mp3"
    final_path = os.path.join(dest_filepath, input_tokens[0] + format)
    os.replace(input_tokens[5], final_path)

if __name__ == "__main__": 
    gui()
    main()
