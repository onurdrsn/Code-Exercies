from googletrans import Translator
import speech_recognition as spr
from gtts import gTTS
import os

reco1= spr.Recognizer()
mc=spr.Microphone()
with mc as source:
    print("Hello, I love you")
    print("~~~~~~~~~~~~~~~~~")
    reco1.adjust_for_ambient_noise(source, duration=0.2)
    audio=reco1.listen(source)
    mytext=reco1.recognize_google(audio)
    mytext=mytext.lower()

    if hello in mytext:
        trans = Translator()
        from_lang = "en"
        to_lang = "tr"

        with mc as source:
            print("Speak...")
            reco1.adjust_for_ambient_noise(source, durtaion=0.2)
            audio=reco1.listen(source)
            get_stence = reco1.recognize_google(audio)
            try:
                print("Phase to be Translated: "+ get_sentence)
                text = text_to_translate.text
                speak = gTTS(text = text, lang = to_lang, slow = False)
                speak = save("capture.mp3")
                os.system("start capture.mp3")
            except spr.UnknownValueError:
                print("Unable to Input")
            except spr.RequestError as e:
                print("Unable to Output".format(e))  

"""text = "seni seviyorum"
translator = Translator()
dt = translator.detect(text)
translated = translator.translate(text)
print(translated.text)"""