import webbrowser, os
from datetime import datetime
import pytz
from tzlocal import get_localzone

utc_dt = datetime(2009, 7, 10, 18, 44, 59, 193982, tzinfo=pytz.utc)
current_time = utc_dt.astimezone(get_localzone())
local_hour = current_time.hour
print(utc_dt)
print(current_time)

## LOCAL_TIMEZONE = datetime.datetime.now(datetime.timezone.utc).astimezone().tzinfo
## that is local timezone in dt

embed_codes_nl = ['ogZOuyEUaqM','6ctYQ2giDfw','rjoi8HzYjnY','alCXAH7tzT4','YsRHAojQK20',
'tnlpjqXHQnI','DHskPDrg-fQ','r7Ncy-yY9Uw','qRAt72y7Dl0','BtxRvNYYUUo','1ZXwbqjoHQ8','_4G7EWJ7Ik8',
'JkHgU_O6f64','yQicvIsa8W8','WalIFXKCmHU','N5Xx8r2uTLI','37UjXU-3wZ8','5QJaWg5fOAo',
'qYhA2QqFDS8','Fksz_uENt9U','ZUPm4MT64VU','YukcuUPS05U','xbjbGNa-7eE','kginZ7__1aE']

hours = list(range(1,25))
new_leaf_tp = dict(zip(hours,embed_codes_nl))

def video_link(hour):
    value = new_leaf_tp[hour]
    link = 'https://www.youtube.com/embed/{}'.format(value)
    return link

#youtube_link = video_link(18)


def create_page(video_url):
    os.chdir(r'C:\Users\Matthew\Desktop')
    filename = 'helloworld.html'
    f = open(filename,'w+')
    message = """<!DOCTYPE html>
    <html>
    This is where some of the text might go 
    <head>
    That is
    </head>

    If I am actually correct

    <body>
    <iframe width="420" height="345" src={URL}>
    </iframe>

    </p></body>
    A little text down here 

    </body>

    Finish it up down here
    </html>"""
    complete_message = message.format(URL=video_url)
    f.write(complete_message)
    f.close()
    return

url = video_link(local_hour)
print(url)
create_page(url)

# webbrowser.open_new_tab(youtube_link)