import os
from pathlib import Path as p

import ffmpeg


class AudioConverter:
    video_extensions = {'.mp4', '.mkv', '.avi', '.mov', '.wmv', '.flv', '.webm'}
    audio_extensions = {'.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', '.m4a'}

    def __init__(self, file_name: str):
        self.file_name = file_name
        self.FFMPEG_BIN = "ffmpeg"
        self.filepath, self.ext = os.path.splitext(self.file_name)

    def convert_to_audio(self, ext: str):
        """
        Converts a input file to mp3

        command: ffmpeg -n -i input.m4a -acodec libmp3lame -ab 128k output.mp3
        """
        ext = '.' + ext.strip('.')
        if self.ext == ext:
            return
        output_file = str(p(self.file_name).with_suffix('').with_suffix(ext))
        input_stream = ffmpeg.input(self.file_name)
        file_ext = p(self.file_name).suffix
        if file_ext in AudioConverter.video_extensions:
            output_stream = ffmpeg.output(input_stream.audio, output_file)
        else:
            output_stream = ffmpeg.output(input_stream, output_file)
        # Set the codec and format options
        output_stream = output_stream.global_args('-hwaccel', 'cuvid')
        # Run the conversion
        ffmpeg.run(output_stream)
