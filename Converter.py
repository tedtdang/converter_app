import os
import logging
import logging.handlers
import subprocess as sp
import json
from multiprocessing.pool import ThreadPool


class AudioConverter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.FFMPEG_BIN = "ffmpeg"
        self.filepath, self.ext = os.path.splitext(self.file_name)

    def convert_to_m4a(self):
        """
        Converts a input file to m4a

        command: ffmpeg -i input.wav -c:a aac -b:a 160k output.m4a
        ffmpeg -i input.wav -c:a aac -b:a 160k output.m4a
        """
        codec = "aac"
        m4a_filename = self.filepath + ".m4a"
        command = [self.FFMPEG_BIN,
                   "-n",
                   "-i", self.file_name,
                   "-acodec", codec,
                   "-ab", "128k",
                   m4a_filename
                   ]

        return command

    def convert_to_mp3(self):
        """
        Converts a input file to mp3

        command: ffmpeg -n -i input.m4a -acodec libmp3lame -ab 128k output.mp3
        """
        if self.ext == ".mp3":
            return

        codec = "libmp3lame"
        mp3_filename = self.filepath + ".mp3"

        command = [self.FFMPEG_BIN,
                   "-n",
                   "-i", self.file_name,
                   "-acodec", codec,
                   "-ab", "128k",
                   mp3_filename
                   ]
        return command

    def convert_to_ogg(self):
        """
        Converts a input file to ogg

        command: ffmpeg -n -i input.m4a -acodec libvorbis -aq 60 -vn -ac 2 output.ogg
        """
        if self.ext == ".ogg":
            return

        codec = "libvorbis"
        ogg_filename = self.filepath + ".ogg"

        command = [self.FFMPEG_BIN,
                   "-n",
                   "-i", self.file_name,
                   "-acodec", codec,
                   "-aq", "60",
                   "-vn",
                   "-ac", "2",
                   ogg_filename
                   ]

        return command