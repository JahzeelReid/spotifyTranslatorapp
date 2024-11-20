import re
from datetime import datetime
import grabber as grabber
import lyrictesting as lyrictesting


from flask import Flask

app = Flask(__name__)


@app.route("/profile")
def home():
    # print("http://127.0.0.1:5000/profile")
    # 1 should show the song name, song picture, author
    # 2 should list next lyric(requires times sync)
    # starting with 1
    playinginfo = grabber.checkPlaying() #returns [name, author, album, duration, imagesrc]
    lyriclist = None
    if playinginfo:
        # lyriclist = lyrictesting.getsyncLyric(playinginfo[0],playinginfo[1],playinginfo[2],playinginfo[3])
        lyriclist = grabber.recentlyric(playinginfo[0],playinginfo[1],playinginfo[2],playinginfo[3], playinginfo[5])

    body = {
        "lyric" : lyriclist,
        "songname" : playinginfo[0],
        "author" : playinginfo[1],
        "albumname" : playinginfo[2],
        "imgsrc" : playinginfo[4],

    }
    return body

@app.route("/play")
def play():
    # print("http://127.0.0.1:5000/profile")
    # 1 should show the song name, song picture, author
    # 2 should list next lyric(requires times sync)
    # starting with 1
    playinginfo = grabber.checkPlaying() #returns [name, author, album, duration, imagesrc]
    lyriclist = None
    if playinginfo:
        lyriclist = lyrictesting.getsyncLyric(playinginfo[0],playinginfo[1],playinginfo[2],playinginfo[3])

    body = {
        "lyric" : lyriclist,
        "songname" : playinginfo[0],
        "author" : playinginfo[1],
        "albumname" : playinginfo[2],
        "imgsrc" : playinginfo[4],

    }
    return body



@app.route("/")
def my_profile():
    lyriclist = grabber.litmustest()
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript",
        "lyric" : lyriclist
    }

    return response_body
