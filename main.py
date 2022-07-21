from ast import arg
from doctest import ELLIPSIS_MARKER
from pytube import YouTube
from pytube.cli import on_progress
from sys import argv
import os

if __name__ == "__main__":
    if len(argv) == 1:
        print("You need to give me a link:)")
    else:
        link = argv[1]
        yt = YouTube(link, on_progress_callback=on_progress)

        print("Title: ", yt.title)
        print("Creator: ", yt.author)
        print("Views: ", yt.views)
        print(f"Length: { yt.length } sek.")

        yd = yt.streams.get_highest_resolution()
        yd.download("D:\Videos\YouTube")

        os.system("pause")