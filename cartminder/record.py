from persistqueue import SQLiteQueue
from cartminder.speech_recognition import VoskSmallRecognizer
from cartminder.sound_capture import VolumeSoundCapturer
from cartminder.settings import settings

if __name__ == "__main__":
    output_queue = SQLiteQueue(
        settings.storage_path,
        db_file_name="recordings.db"
    )

    print("Loading capturer...")
    capturer = VolumeSoundCapturer()
    
    print("Loading recognizer...")
    recognizer = VoskSmallRecognizer()

    print("Listening...")
    for capture in capturer.listen():
        text = recognizer.recognize(capture, capturer.sample_rate)
        print(text)
