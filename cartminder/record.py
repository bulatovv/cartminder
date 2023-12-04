from cartminder.recording.sound_capture import VolumeSoundCapturer
from cartminder.recording.filesystem_wav_recorder import FilesystemWavRecorder
from cartminder.settings import settings

if __name__ == "__main__":
    capturer = VolumeSoundCapturer()
    recorder = FilesystemWavRecorder(VolumeSoundCapturer(), settings.recordings_storage_path)

    recorder.record()
