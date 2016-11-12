import urllib


def read_text():
    quotes = open('/users/zibi/Desktop/Python Projects/movie_quotes.txt')
    contents_of_file = quotes.read()
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen('http://www.wdylike.appspot.com/?q=' + text_to_check)
    output = connection.read()
    connection.close()
    if 'true' in output:
        print('Profanity Alert!!')
    elif 'false' in output:
        print('No profanity detected. Good to go!')
    else:
        print('There was an error scanning the document.')


read_text()
