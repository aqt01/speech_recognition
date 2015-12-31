import speech_recognition as sr
import re
import os

# obtain audio from the import microphone
r = sr.Recognizer()

# Language/Dialect to use. Uncomment/Comment for the desired one

# lang="es-ES" #->  Espanol/Espana
lang="en-US" #-> English/US


# Regular expressions

if (lang=="en-US"):
    call='[Cc]all*'
    msg='[Mm]essag*'
    body_msg='[Tt]ell*'

elif (lang=="es-ES"):
    call='[Ll]ama*'
    msg='[Mm]ensaj*'
    body_msg='[Dd]i*'

# Using default micro in OS as source
with sr.Microphone() as source:
    print("Say something! ")
    audio = r.listen(source)
    
    #Flag variable for messaging command
    x=0

    #Flag variable for call command
    pos=0

    # Speech Recognition
    txt = r.recognize_google(audio,language=lang)


    # Detection command "Call"

    try:
        pos = re.search(call,txt).start() 
    except Exception:
        pos = -1
        pass
    
    # Detecting command "Message"
    
    try:
        x = re.search(msg,txt).start() 
        wr = re.search(body_msg,txt).start() 

    except Exception:
        x = -1
        pass
    
    #Number extraction 

    numb = ''
    
    for s in txt:
        if s.isdigit():
            numb=numb+s

    # ADB stuff for call x number
    if pos!=-1:
        print(numb)
        os.system("adb kill-server")
        os.system("adb start-server")
    #   os.system('adb connect 192.168.1.12:5555') uncheck if your cellphone is on adb wifi
        print ("J.A.R.V.I.S.: Calling: "+ str(numb))
        os.system("adb shell am start -a android.intent.action.CALL -d tel:"+numb)
       
    # ADB stuff for messaging x number
    if x!=-1:
        
        # Take all text after the command Say or specified in body_msg var
        print x
        print wr
        msg = txt[x:len(txt)]
        c=0

        print msg
        
        for a in msg:
            c=c+1
            
            if(a==' '):
                wr=wr+c
                break
        
        msg= txt[wr:len(txt)]
        msg= msg.replace(" ","\ ")
        
        print "enssaging"
        print numb+" "+msg
        os.system("adb kill-server")
        os.system("adb start-server")
        message_command='adb shell am start -a android.intent.action.SENDTO -d sms:DO'+numb+' --es sms_body "'+msg+'" --ez exit_on_sent true'
        
        os.system(message_command) 

        # This stuff is for sending pressing buttons to send message. You may lose mins
        os.system("adb shell input keyevent 22")
        os.system('adb shell input keyevent 66')


   
# Debug Purposes
try:
    print ("\n")
    print("You said:" + r.recognize_google(audio, language=lang))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google import Speech Recognition service; {0}".format(e))

