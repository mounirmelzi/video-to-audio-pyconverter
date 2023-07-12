import os
import shutil
from moviepy.editor import VideoFileClip


class Converter:
    def __init__(self, video_path: str) -> None:
        self.video_path = video_path

    def convert(self, output_dir: str, audio_extension: str = ".mp3") -> None:
        output_path = os.path.join(output_dir, self.get_filename() + audio_extension)

        video = VideoFileClip(self.video_path)
        audio = video.audio
        audio.write_audiofile(output_path)

    def get_filename(self) -> str:
        video_filename = os.path.basename(self.video_path)
        filename = os.path.splitext(video_filename)[0]
        return filename

    @staticmethod
    def convert_folder(folder_path: str, extension: str) -> None:
        audio_folder = os.path.join(folder_path, "output")

        if os.path.exists(audio_folder):
            shutil.rmtree(audio_folder)

        files = os.listdir(folder_path)

        os.makedirs(audio_folder, exist_ok=True)

        for filename in files:
            converter = Converter(video_path=os.path.join(folder_path, filename))
            converter.convert(output_dir=audio_folder, audio_extension=extension)
