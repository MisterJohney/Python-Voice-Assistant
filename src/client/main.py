from sender import send_file
from recorder import listen_for_keyword, record_audio_until_silence

import logging

import os
# from playsound3 import playsound

INPUT_FILE = "./recording.wav"
OUTPUT_FILE = "./output.mp3"
KEYWORD = "start"

if __name__ == "__main__":
    logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

    logging.debug("Started")
    while True:
        listen_for_keyword(KEYWORD)
        logging.info("Recording audio")
        record_audio_until_silence(INPUT_FILE)

        logging.info("Sending file")
        send_file(INPUT_FILE)

        # NOTE: on the desktop for me the audio isn't playing
        logging.info("Playing")
        # playsound(OUTPUT_FILE)
        os.system("mpv --speed=1.5 " + OUTPUT_FILE) # If edditing cmd arguments, always leave a trailing space
