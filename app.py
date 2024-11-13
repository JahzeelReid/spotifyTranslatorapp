import re
from datetime import datetime
import grabber as grabber
import lyrictesting as lyrictesting


from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    # print("http://127.0.0.1:5000/profile")
    # 1 should show the song name, song picture, author
    # 2 should list next lyric(requires times sync)
    # starting with 1
    playinginfo = grabber.checkPlaying() #returns [name, author, album, duration, imagesrc]
    lyriclist = lyrictesting.getplainLyric(playinginfo[0],playinginfo[1],playinginfo[2],playinginfo[3])

    body = {
        "lyric" : lyriclist,
        "songname" : playinginfo[0],
        "author" : playinginfo[1],
        "albumname" : playinginfo[2],
        "imgsrc" : playinginfo[4]
    }
 
    return body


@app.route("/hello/<name>")
def hello_there(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", name)

    if match_object:
        clean_name = match_object.group(0)
    else:
        clean_name = "Friend"

    content = "Hello there, " + clean_name + "! It's " + formatted_now
    return content

@app.route('/profile')
def my_profile():
    lyriclist = grabber.litmustest()
    response_body = {
        "name": "Nagato",
        "about" :"Hello! I'm a full stack developer that loves python and javascript",
        "lyric" : lyriclist
    }

    return response_body
