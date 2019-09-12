EMBED_CODES_FILE = ['config_files', 'embed_codes.txt']
TEMPLATE_FILE = ['config_files', 'template.html']
OUTPUT_FILE = ['output_files', 'webpage.html']

def configure_paths():
    '''
    Handle different environments with different path separators ('/' vs '\' in paths)

    P.S. This stuff is why you want to consider a config file. For further reading,
    checkout the configparse module.
    '''
    from os.path import join

    global EMBED_CODES_FILE
    global TEMPLATE_FILE
    global OUTPUT_FILE

    EMBED_CODES_FILE = join(*EMBED_CODES_FILE)
    TEMPLATE_FILE = join(*TEMPLATE_FILE)
    OUTPUT_FILE = join(*OUTPUT_FILE)

def display_page():
    '''
    Display a webpage with an appropriate link based on the hour of the day.
    '''
    video_url = get_video_url()
    create_page(video_url)
    
    from webbrowser import open_new_tab
    open_new_tab(OUTPUT_FILE)

def create_page(video_url):
    template = get_template_file()
    page = None

    with open(OUTPUT_FILE, 'w') as output_file:
        page = template.format(URL=video_url)
        output_file.write(page)

def get_template_file():
    '''
    Simply loads the template file and returns the string.
    '''
    with open(TEMPLATE_FILE, 'r') as template:
        return template.read()

def get_video_url():
    '''
    Return a YouTube embed url based on the hour of the day.
    '''
    import datetime

    embed_codes = get_embed_codes()
    current_time = datetime.datetime.now()
    index = (current_time.hour - 1) % 24
    return 'https://www.youtube.com/embed/{}?'.format(embed_codes[index])

def get_embed_codes():
    '''
    Load a list of 24 embed codes from a file.
    '''
    with open(EMBED_CODES_FILE, 'r') as embed_file:
        return [line.strip() for line in embed_file]

if __name__ == '__main__':
    configure_paths()
    display_page()