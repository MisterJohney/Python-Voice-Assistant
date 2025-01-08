from sender import send_file

import logging

from playsound3 import playsound

INPUT_FILE = "../tests/recording.wav"
OUTPUT_FILE = "../tests/compleation.mp3"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    logging.info("Sending file")
    send_file(INPUT_FILE)

    # NOTE: on the desktop for me the audio isn't playing
    logging.info("Playing")
    playsound(OUTPUT_FILE)
