from Converter import AudioConverter

audio_file = './original audio.mp3'
video_file = "./original video.mp4"

converter = AudioConverter(audio_file)
converter.convert_to_audio(ext='mp3')
