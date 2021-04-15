import datetime
import greetings as gr
import recogniseSpeech as rs
import event_handler as event

if __name__ == '__main__':
    gr.greet()
    cTime=datetime.datetime.now().minute
    while 1:
        query = rs.takeCommand().lower()
        print(datetime.datetime.now().minute)

        # if datetime.datetime.now().minute < cTime+1 or ('hey' in query):
        if True:
            cTime = datetime.datetime.now().minute
            event.handle_event(query)
        else:
            print('Something is not right')
