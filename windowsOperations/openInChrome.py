import webbrowser
def openURL(url):
    if 'youtube' in url:
        webbrowser.open("www.youtube.com")
    elif 'google' in url:
        webbrowser.open("www.google.com")
    elif 'cricbuzz' in url:
        webbrowser.open("www.cricbuzz.com")
    elif 'whatsapp' in url:
        webbrowser.open("https://web.whatsapp.com/")
    elif 'facebook' in url:
        webbrowser.open("www.facebook.com")
    elif 'twitter' in url:
        webbrowser.open("www.twitter.com")
    elif 'mail' in url:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
def searchString(st):
    webbrowser.open("www.google.com/search?q="+st)