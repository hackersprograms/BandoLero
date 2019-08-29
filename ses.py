import speech_recognition as sr

def ses():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("söyle bakalım")
        audio=r.listen(source)

    try:
        gelen=str(r.recognize_google(audio))
        if(gelen.find("merhaba")!=-1):
            print("merhaba")
        elif(gelen.find("nasılsın")!=-1):
            print("iyiyimsen nasılsın")
    except:
        print("bir hata oldu")
while 1:
    ses()
