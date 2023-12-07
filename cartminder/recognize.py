from persistqueue import SQLiteQueue
from cartminder.speech_recognition import VoskSmallRecognizer
from cartminder.settings import settings

if __name__ == "__main__":
    input_queue = SQLiteQueue(
        settings.storage_path,
        db_file_name="recordings.db"
    )

    output_queue = SQLiteQueue(
        settings.storage_path,
        db_file_name="transcriptions.db"
    )

    recognizer = VoskSmallRecognizer()

    while True:
        capture = queue.get()
        text = recognizer.recognize(capture))
        output_queue.put(text)


