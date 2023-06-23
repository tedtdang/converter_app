from Converter import AudioConverter
from pathlib import Path as p
import moviepy.editor as mp
from pydub import AudioSegment
import subprocess as sp

audio_file = './original audio.ogg'
video_file = "./original video.mp4"
output_ext = '.mp3'

converter = AudioConverter(audio_file)
sp.run(converter.convert_to_mp3())