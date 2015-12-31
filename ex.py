
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import re

# obtain audio from the import microphone


#!/usr/bin/env python

r = sr.Recognizer()


with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
#    import ipdb
#    ipdb.set_trace()
    x=0
    pos=0

    txt = ''
    try:
        txt = r.recognize_google(audio,language="es-ES")
        print 'usted desea llamar: ' + txt

        pos = re.search("[Ll]ama*",txt).start() 
    except Exception:
        pos = -1
        pass
    
    try:
        txt = r.recognize_google(audio,language="es-ES")
        print 'usted desea enviar mensaje a: ' + txt

        x = re.search("[Mm]ensaje*",txt).start() 
        wr = re.search("[Ee]scribe*",txt).start() 

    except Exception:
        x = -1
        pass
    


    print (txt)
    print (pos)
    
    
    numb = ''
    
    for s in txt:
        if s.isdigit():
            numb=numb+s




    if pos!=-1:
        print(numb)
        import os
        os.system("adb kill-server")
        os.system("adb start-server")
    #    os.system('adb connect 192.168.1.12:5555')
        os.system("adb shell am start -a android.intent.action.CALL -d tel:"+numb)
    if x!=-1:
        import os

        xs = txt[wr:len(txt)]
        c=0
        
        for a in xs:
            c=c+1
            if(a==' '):
                wr=wr+c
                break
        
        mensaje = txt[wr:len(txt)]
        print mensaje
        mensaje = mensaje.replace(" ","\ ")
        print numb
        #os.system("adb kill-server")
        os.system("adb start-server")
        print "a que numero desea enviar el sms?"
        xz='adb shell am start -a android.intent.action.SENDTO -d sms:DO'+numb+' --es sms_body "'+mensaje+'" --ez exit_on_sent true'
        print xz
        os.system('adb shell am start -a android.intent.action.SENDTO -d sms:DO'+numb+' --es sms_body "'+mensaje+'" --ez exit_on_sent true') 
        os.system("adb shell input keyevent 22")
        os.system('adb shell input keyevent 66')


    print ("J.A.R.V.I.S.: Llamando a:" + str(numb))



# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`
    print("Google Speech Recognition thinks you said " + r.recognize_google(audio, language="es-ES"))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google import Speech Recognition service; {0}".format(e))
'''
# recognize speech using Wit.ai
WIT_AI_KEY = "INSERT WIT.AI API KEY HERE" # Wit.ai keys are 32-character uppercase alphanumeric strings
try:
    print("Wit.ai thinks you said " + r.recognize_wit(audio, key=WIT_AI_KEY))
except sr.UnknownValueError:
    print("Wit.ai could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Wit.ai import service; {0}".format(e))

# recognize speech using IBM Speech to Text
IBM_USERNAME = "INSERT IBM SPEECH TO TEXT USERNAME HERE" # IBM Speech to Text usernames are strings of the form XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX
IBM_PASSWORD = "INSERT IBM SPEECH TO TEXT PASSWORD HERE" # IBM Speech to Text passwords are mixed-case alphanumeric strings
try:
    print("IBM Speech to Text thinks you said " + r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD))
except sr.UnknownValueError:
    print("IBM Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from IBM import Speech to Text service; {0}".format(e))

# recognize speech using AT&T Speech to Text
ATT_APP_KEY = "INSERT AT&T SPEECH TO TEXT APP KEY HERE" # AT&T Speech to Text app keys are 32-character lowercase alphanumeric strings
ATT_APP_SECRET = "INSERT AT&T SPEECH TO TEXT APP SECRET HERE" # AT&T Speech to Text app secrets are 32-character lowercase alphanumeric strings
try:
    print("AT&T Speech to Text thinks you said " + r.recognize_att(audio, app_key=ATT_APP_KEY, app_secret=ATT_APP_SECRET))
except sr.UnknownValueError:
    print("AT&T Speech to Text could not understand audio")
except sr.RequestError as e:
    print("Could not request results from AT&T Speech to Text service; {0}".format(e))
    '''
