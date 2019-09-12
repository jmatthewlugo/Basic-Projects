import webbrowser, os
import datetime as dt

current_time = dt.datetime.now()
current_hour = current_time.hour

embed_codes_nl = ['ogZOuyEUaqM','6ctYQ2giDfw','rjoi8HzYjnY','alCXAH7tzT4','YsRHAojQK20',
'tnlpjqXHQnI','DHskPDrg-fQ','r7Ncy-yY9Uw','qRAt72y7Dl0','BtxRvNYYUUo','1ZXwbqjoHQ8','_4G7EWJ7Ik8',
'JkHgU_O6f64','yQicvIsa8W8','WalIFXKCmHU','N5Xx8r2uTLI','37UjXU-3wZ8','5QJaWg5fOAo',
'qYhA2QqFDS8','Fksz_uENt9U','ZUPm4MT64VU','YukcuUPS05U','xbjbGNa-7eE','kginZ7__1aE']

hours = list(range(1,25))
new_leaf_tp = dict(zip(hours,embed_codes_nl))

def video_link(hour):
    value = new_leaf_tp[hour]
    link = 'https://www.youtube.com/embed/{}?'.format(value)
    print(value)
    return link

def create_page(video_url):
    filename = 'helloworld.html'
    f = open(filename,'w+')
    message = """<!DOCTYPE html5>
    <html>
    <head>

    <title> Name of page here I guess </title>
    </head>
    <body>
 
    <iframe width="420" height="315" src={URL}>
    </iframe>
    
    <p>
    <h1>If I am actually correct</h1>
    </p>

    <p2>
    <h2>A little text down here</h2>
    </p2>
    
    <p3>
    <h3>Finish it up down here</h3>
    </p3>
    
    </body>
    </html>"""

    complete_message = message.format(URL=video_url)
    f.write(complete_message)
    f.close()
    page = webbrowser.open_new_tab(filename)
    return page

url = video_link(current_hour)
post = create_page(url)

print(url)
