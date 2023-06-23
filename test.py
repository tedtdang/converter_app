from Converter import AudioConverter
import subprocess as sp

audio_file = './original audio.mp3'
video_file = "./original video.mp4"
output_ext = '.mp3'

converter = AudioConverter(audio_file)
# sp.run(converter.convert_to_mp3())
# sp.run(converter.convert_to_ogg())
# sp.run(converter.convert_to_audio('wav'))