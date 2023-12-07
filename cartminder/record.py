from cartminder.speech_recognition import VoskSmallRecognizer
from cartminder.sound_capture import VolumeSoundCapturer
from cartminder.settings import settings

import requests

if __name__ == "__main__":
    print("Loading capturer...")
    capturer = VolumeSoundCapturer()
    
    print("Loading recognizer...")
    recognizer = VoskSmallRecognizer()

    print("Listening...")
    for capture in capturer.listen():
        text = recognizer.recognize(capture, capturer.sample_rate)
       
        params = {
            "chat_id": settings.chat_id,
            "text": text
        }
        r = requests.get("https://api.telegram.org/bot{}/sendMessage".format(settings.bot_token), params=params)
        
        print(r.status_code)
        print(text)
