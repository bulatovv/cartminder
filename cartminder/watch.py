from cartminder.recording.filesystem_recordings_watcher import FilesystemRecodingsWatcher
from cartminder.speech_recognition.vosk_small_recognizer import VoskSmallRecognizer
from cartminder.settings import settings
import requests


if __name__ == "__main__":
    recognizer = VoskSmallRecognizer()
    watcher = FilesystemRecodingsWatcher(settings.recordings_storage_path)

    for item in watcher.watch():
        data, sample_rate = item
        message_text = recognizer.recognize(data, sample_rate)

        send_message_url = (
                f'https://api.telegram.org/bot{settings.bot_token}/sendMessage'
                f'?chat_id={settings.chat_id}&text={message_text}'
        )
        response = requests.get(send_message_url)
        print(response.json())
