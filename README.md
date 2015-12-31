# Basic Speech Recognizer with Python 

A demo implementation of voice recognition  written in python(2.7) to send commands through adb in android.

The program main lib is [SpeechRecognition 3.1.3](https://pypi.python.org/pypi/SpeechRecognition/) which uses 
Google Speech Recognition service as Speech Recognizer.  The *command detection* is done manually using regular expressions over
the text output from the Speech Recognizer.
 
 The program works as follows:
 
 *Voice* > *Speech Recognition* > *Command Detection* > *Action through adb*
 

## Features
> Send messages
> Calls

## Use

python ex.py

## Voice Commands

Here we show some examples in english and spanish voice commands.

* [Command synonimous or conjugations] [(Regular Expression)]

### Spanish
* "Llamar", "Llamando", "Llama".. ( [Ll]amar* )
* "Mensaje"... ( [Mm]ensaje)
* "Escribe", "Escriba", "Escribale" ... ( [Ee]scrib* )

### English
* "Call", "Calling"... ([Cc]all*)
* "Message" ... ([Mm]essag*)
* "Write" ... ([Ww]rit*)
* "Say"... ([Ss]a*)

### Example

* Say: "Please call X (number)" or "Send x(number) message saying I love you "
* Diga: "LLama a X(numero)" o "Envia mensaje al numero x(numero) escribe "Te amo" " 


## Requirements
* Internet (for the speech recognition service)
* Must have adb installed on system
* For python libs check [Requirements.txt] (https://github.com/aqt01/speech_recognition/blob/master/requirements.txt)



## TODO
> Send messages via whatsapp
> Send GeoLocation
> Use wit.ai as voice interface
> Apply software principles to the project 
> ...
