import webbrowser
import event_handler as event


def open_url(url):
    if 'youtube' in url:
        webbrowser.open("www.youtube.com")
    elif 'google' in url:
        webbrowser.open("www.google.com")
    elif 'github' in url:
        webbrowser.open("https://github.com/SidharthSoumya")
    elif 'linkedin' in url:
        webbrowser.open("https://www.linkedin.com/in/j-soumya-sidharth-88645a7a/")
    elif 'cricbuzz' in url:
        webbrowser.open("www.cricbuzz.com")
    elif 'whatsapp' in url:
        webbrowser.open("https://web.whatsapp.com/")
    elif 'facebook' in url:
        webbrowser.open("www.facebook.com")
    elif 'twitter' in url:
        webbrowser.open("www.twitter.com")
    elif 'code' in url:
        event.vs_code()
    elif 'mail' in url:
        webbrowser.open("https://mail.google.com/mail/u/0/#inbox")


def search(st):
    webbrowser.open("www.google.com/search?q="+st)
